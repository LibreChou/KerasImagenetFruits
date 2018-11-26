# Trains a model for 4 epochs: 12x12 shifts. Size of image trainable 224x224. with shifts of 12x12, target size is 235
#
# To run:
#   model = t_v49.trainModel(epochs=200)

from DataGen import DataGen_v1_150x150_1frame as dg_v1 
from DataGen import AugSequence_v3_randomcrops as as_v3
from Model import Model_v9_noDropout as m_v9
import time
from Evaluation import Eval_v2_top5accuracy as e_v2
from Evaluation import Eval_v3_5framesaccuracy as e_v3
from Evaluation import Eval_v4_10framesaccuracy as e_v4
from keras.callbacks import EarlyStopping


def trainModel( model = None, epochs = 1):
    # Trains a model
    #   model = optional parameter; creates new if not passed; otherwise keeps training
    #   epochs - number of max epochs to train (subject to early stopping)
    # Returns: 
    #   model: trained Keras model

    crop_range = 32 # number of pixels to crop image (if size is 235, crops are 0-223, 1-224, ... 11-234)
    target_size = 224
    datasrc = "ilsvrc14_50classes"
    #datasrc = "ilsvrc14"

    #dataGen = dg_v1.prepDataGen(target_size = target_size, batch_size = 64 )
    dataGen = as_v3.AugSequence ( target_size=target_size, crop_range=crop_range, batch_size=128, datasrc=datasrc, test=False, debug=True )

    if model is None:
        input_shape = (target_size, target_size, 3)
        model = m_v9.prepModel ( input_shape = input_shape, \
            L1_size_stride_filters = (11, 4, 96), L1MaxPool_size_stride = (3, 2), \
            L2_size_stride_filters = (5, 1, 256), L2MaxPool_size_stride = (3, 2), \
            L3_size_stride_filters = (3, 1, 384), \
            L4_size_stride_filters = (3, 1, 384), \
            L5_size_stride_filters = (3, 1, 256), L5MaxPool_size_stride = (3, 2), \
            D1_size = 4096, \
            D2_size = 4096, \
            Softmax_size = 50, \
            Conv_padding = "same" )

    #epochs = 0

    #prepare a validation data generator, used for early stopping
    vldDataGen = dg_v1.prepDataGen( target_size=target_size, test=True, batch_size=128, datasrc=datasrc )
    callback_earlystop = EarlyStopping ( monitor='acc', min_delta=0.001, patience=20, verbose=1, mode='max', restore_best_weights=True )

    # full epoch is 12x12 = 144 passes over data: 1 times for each subframe
    model.fit_generator ( dataGen, steps_per_epoch=len(dataGen), epochs=epochs, verbose=2, validation_data=vldDataGen, validation_steps=len(vldDataGen), callbacks=[callback_earlystop] )
    #model.fit_generator ( dataGen, steps_per_epoch=1, epochs=epochs, verbose=2, validation_data=vldDataGen, validation_steps=len(vldDataGen), callbacks=[callback_earlystop] )
    #model.fit_generator ( dataGen, steps_per_epoch=len(dataGen), epochs=epochs, verbose=2 )
    #model.fit_generator ( dataGen, steps_per_epoch=1, epochs=epochs, verbose=2 )

    print ("Evaluation on train set (1 frame)")
    e_v2.eval(model, target_size=target_size, datasrc=datasrc)
    print ("Evaluation on validation set (1 frame)")
    e_v2.eval(model, target_size=target_size, datasrc=datasrc, test=True)
    print ("Evaluation on validation set (5 frames)")
    e_v3.eval(model, target_size=target_size, datasrc=datasrc, test=True)
    print ("Evaluation on validation set (10 frames)")
    e_v4.eval(model, target_size=target_size, datasrc=datasrc, test=True)

    return model