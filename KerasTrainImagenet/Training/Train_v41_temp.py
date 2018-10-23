# Trains a model for 4 epochs: 12x12 shifts. Size of image trainable 224x224. with shifts of 12x12, target size is 235
#
# To run:
#   model = t_v41.trainModel()

from DataGen import DataGen_v1_150x150_1frame as dg_v1 
from DataGen import AugSequence as as_v1
from Model import Model_v7_5cnn as m_v7
import time
from Evaluation import Eval_v1_simple as e_v1
from Evaluation import Eval_v2_top5accuracy as e_v2

def trainModel( model = None):
    # Trains a model
    #   model = optional parameter; creates new if not passed; otherwise keeps training
    # Returns: 
    #   model: trained Keras model

    crop_range = 1 # number of pixels to crop image (if size is 235, crops are 0-223, 1-224, ... 11-234)
    target_size = 224
    datasrc = "ilsvrc14"

    #dataGen = dg_v1.prepDataGen(target_size = target_size, batch_size = 64 )
    dataGen = as_v1.AugSequence ( target_size=target_size, crop_range=crop_range, batch_size=256, datasrc=datasrc, test=False, debug=True )

    if model is None:
        input_shape = (224, 224, 3)
        model = m_v7.prepModel ( input_shape = input_shape, \
            L1_size_stride_filters = (7, 2, 96), L1MaxPool_size_stride = (3, 2), \
            L2_size_stride_filters = (5, 2, 256), L2MaxPool_size_stride = (3, 2), \
            L3_size_stride_filters = (3, 1, 384), \
            L4_size_stride_filters = (3, 1, 384), \
            L5_size_stride_filters = (3, 1, 256), L5MaxPool_size_stride = (3, 2), \
            D1_size = 4096, \
            D2_size = 4096)

    full_epochs = 2 # 1 epoch is full pass of data over all variants of 16x16 shifts
                    #  12x12 = 144 passes through original images in 1 full epoch

    # full epoch is 12x12 = 144 passes over data: 1 times for each subframe
    model.fit_generator ( dataGen, steps_per_epoch=len(dataGen), epochs=full_epochs, verbose=2 )

    e_v2.eval(model, target_size=target_size, datasrc=datasrc)
    e_v2.eval(model, target_size=target_size, datasrc=datasrc, test=True)

    return model