# Prepares a simple model
#   Sample downloaded from https://elitedatascience.com/keras-tutorial-deep-learning-in-python
#
# To run: 
#   model = m_v10.prepModel()
# To load a trained model:
#   model = load_model("D:\ILSVRC14\models\model_v55.h5", custom_objects={'top_5': m_v11.top_5})

from keras.models import Model
from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.optimizers import SGD
from keras.metrics import top_k_categorical_accuracy
from keras.applications.vgg16 import VGG16

def prepModel( train_d1=False, train_d2=False, Softmax_size = 100 ) :

    # Load pretrained model - except the last softmax layer
    base_model = VGG16(  )

    # Remove last (softmax) layer
    base_model.layers.pop()

   
    # Add a softmax layer with 100 classes
    predictions = Dense( Softmax_size , activation='softmax')( base_model.layers[-1].output )

    # this is the model we will train
    model = Model( inputs=base_model.input, outputs=predictions )

    # first: train only the top layers 
    for layer in base_model.layers:
        layer.trainable = False

    d2_layer_index = len(base_model.layers)-1
    base_model.layers [d2_layer_index].trainable = train_d2

    d1_layer_index = len(base_model.layers)-2
    base_model.layers [d1_layer_index].trainable = train_d1
 
    optimizer = SGD(lr=0.01, momentum=0.0, decay=0.0, nesterov=False)

    #def top_5(y_true, y_pred):
    #    return top_k_categorical_accuracy(y_true, y_pred, k=5)

    model.compile(loss='categorical_crossentropy',
              optimizer=optimizer,
              metrics=['accuracy', top_5])

    return model

def top_5(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=5)
