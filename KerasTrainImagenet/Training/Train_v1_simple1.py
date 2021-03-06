# Trains a model for 50 epochs
#
# To run:
#   model = t_v1.trainModel()

from DataGen import DataGen_v1_150x150_1frame as dg_v1 
from Model import Model_v1_simple1 as m_v1

def trainModel():
    # Trains a model
    #
    # Returns: 
    #   model: trained Keras model

    dataGen = dg_v1.prepDataGen()

    model = m_v1.prepModel()

    epochs = 50

    model.fit_generator ( dataGen, steps_per_epoch=len(dataGen), epochs=epochs, verbose=1 )

    # model.save("Train_v1_simple1.h5")
    # model = load_model("Train_v1_simple1.h5")

    return model