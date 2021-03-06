# Prepares a simple model
#   Sample downloaded from https://elitedatascience.com/keras-tutorial-deep-learning-in-python
#
# To run: 
#   model = m_v10.prepModel()
# To load a trained model:
#   model = load_model("D:\ILSVRC14\models\model_v55.h5", custom_objects={'top_5': m_v10.top_5})

from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.optimizers import SGD
from keras.metrics import top_k_categorical_accuracy

def prepModel( input_shape=(224,224,3), \
    L1_size_stride_filters = (3, 1, 64),  L1MaxPool_size_stride = (2, 2), L1_dropout = 0.0, \
    L2_size_stride_filters = (3, 1, 128), L2MaxPool_size_stride = (2, 2), L2_dropout = 0.0, \
    L3_size_stride_filters = (3, 1, 256),                                 L3_dropout = 0.0, \
    L4_size_stride_filters = (3, 1, 256), L4MaxPool_size_stride = (2, 2), L4_dropout = 0.0, \
    L5_size_stride_filters = (3, 1, 512),                                 L5_dropout = 0.0, \
    L6_size_stride_filters = (3, 1, 512), L6MaxPool_size_stride = (2, 2), L6_dropout = 0.0, \
    L7_size_stride_filters = (3, 1, 512),                                 L7_dropout = 0.0, \
    L8_size_stride_filters = (3, 1, 512), L8MaxPool_size_stride = (2, 2), L8_dropout = 0.0, \
    D1_size = 4096,                                                       D1_dropout = 0.5, \
    D2_size = 4096,                                                       D2_dropout = 0.5, \
    Softmax_size = 100, \
    Conv_padding = "same" ) :

    L1_size = L1_size_stride_filters[0]
    L1_stride = L1_size_stride_filters[1]
    L1_filters = L1_size_stride_filters[2]

    L2_size = L2_size_stride_filters[0]
    L2_stride = L2_size_stride_filters[1]
    L2_filters = L2_size_stride_filters[2]

    L3_size = L3_size_stride_filters[0]
    L3_stride = L3_size_stride_filters[1]
    L3_filters = L3_size_stride_filters[2]

    L4_size = L4_size_stride_filters[0]
    L4_stride = L4_size_stride_filters[1]
    L4_filters = L4_size_stride_filters[2]

    L5_size = L5_size_stride_filters[0]
    L5_stride = L5_size_stride_filters[1]
    L5_filters = L5_size_stride_filters[2]

    L6_size = L6_size_stride_filters[0]
    L6_stride = L6_size_stride_filters[1]
    L6_filters = L6_size_stride_filters[2]

    L7_size = L7_size_stride_filters[0]
    L7_stride = L7_size_stride_filters[1]
    L7_filters = L7_size_stride_filters[2]

    L8_size = L8_size_stride_filters[0]
    L8_stride = L8_size_stride_filters[1]
    L8_filters = L8_size_stride_filters[2]

    model = Sequential()
 
    model.add( Convolution2D ( filters = L1_filters,  kernel_size = (L1_size, L1_size),  strides = (L1_stride, L1_stride), padding = Conv_padding, activation='relu',  input_shape=input_shape) )
    if L1_dropout > 0.:
        model.add(Dropout(L1_dropout))
    if L1MaxPool_size_stride is not None:
        L1MaxPool_size = L1MaxPool_size_stride[0]
        L1MaxPool_stride = L1MaxPool_size_stride[1]
        model.add ( MaxPooling2D ( pool_size = ( L1MaxPool_size , L1MaxPool_size ), strides = ( L1MaxPool_stride, L1MaxPool_stride ) ) )

    model.add( Convolution2D ( filters = L2_filters,  kernel_size = (L2_size, L2_size),  strides = (L2_stride, L2_stride), padding = Conv_padding, activation='relu' ) )
    if L2_dropout > 0.:
        model.add(Dropout(L2_dropout))
    if L2MaxPool_size_stride is not None:
        L2MaxPool_size = L2MaxPool_size_stride[0]
        L2MaxPool_stride = L2MaxPool_size_stride[1]
        model.add ( MaxPooling2D ( pool_size = ( L2MaxPool_size , L2MaxPool_size ), strides = ( L2MaxPool_stride, L2MaxPool_stride ) ) )

    model.add( Convolution2D ( filters = L3_filters,  kernel_size = (L3_size, L3_size),  strides = (L3_stride, L3_stride), padding = Conv_padding,  activation='relu' ) )
    if L3_dropout > 0.:
        model.add(Dropout(L3_dropout))

    model.add( Convolution2D ( filters = L4_filters,  kernel_size = (L4_size, L4_size),  strides = (L4_stride, L4_stride), padding = Conv_padding,  activation='relu' ) )
    if L4_dropout > 0.:
        model.add(Dropout(L4_dropout))
    if L4MaxPool_size_stride is not None:
        L4MaxPool_size = L4MaxPool_size_stride[0]
        L4MaxPool_stride = L4MaxPool_size_stride[1]
        model.add ( MaxPooling2D ( pool_size = ( L4MaxPool_size , L4MaxPool_size ), strides = ( L4MaxPool_stride, L4MaxPool_stride ) ) )

    model.add( Convolution2D ( filters = L5_filters,  kernel_size = (L5_size, L5_size),  strides = (L5_stride, L5_stride), padding = Conv_padding,  activation='relu' ) )
    if L5_dropout > 0.:
        model.add(Dropout(L5_dropout))

    model.add( Convolution2D ( filters = L6_filters,  kernel_size = (L6_size, L6_size),  strides = (L6_stride, L6_stride), padding = Conv_padding,  activation='relu' ) )
    if L6_dropout > 0.:
        model.add(Dropout(L6_dropout))
    if L6MaxPool_size_stride is not None:
        L6MaxPool_size = L6MaxPool_size_stride[0]
        L6MaxPool_stride = L6MaxPool_size_stride[1]
        model.add ( MaxPooling2D ( pool_size = ( L6MaxPool_size , L6MaxPool_size ), strides = ( L6MaxPool_stride, L6MaxPool_stride ) ) )

    model.add( Convolution2D ( filters = L7_filters,  kernel_size = (L7_size, L7_size),  strides = (L7_stride, L7_stride), padding = Conv_padding,  activation='relu' ) )
    if L7_dropout > 0.:
        model.add(Dropout(L7_dropout))

    model.add( Convolution2D ( filters = L8_filters,  kernel_size = (L8_size, L8_size),  strides = (L8_stride, L8_stride), padding = Conv_padding,  activation='relu' ) )
    if L8_dropout > 0.:
        model.add(Dropout(L8_dropout))
    if L8MaxPool_size_stride is not None:
        L8MaxPool_size = L8MaxPool_size_stride[0]
        L8MaxPool_stride = L8MaxPool_size_stride[1]
        model.add ( MaxPooling2D ( pool_size = ( L8MaxPool_size , L8MaxPool_size ), strides = ( L8MaxPool_stride, L8MaxPool_stride ) ) )

    model.add(Flatten())
    
    model.add(Dense(D1_size, activation='relu'))
    if D1_dropout > 0.:
        model.add ( Dropout ( D1_dropout ) )
    
    if D2_size is not None:
        model.add (Dense(D2_size, activation='relu'))
        if D2_dropout > 0.:
            model.add ( Dropout ( D2_dropout ) )

    model.add ( Dense ( Softmax_size, activation='softmax' ) )


    optimizer = SGD(lr=0.01, momentum=0.0, decay=0.0, nesterov=False)

    #def top_5(y_true, y_pred):
    #    return top_k_categorical_accuracy(y_true, y_pred, k=5)

    model.compile(loss='categorical_crossentropy',
              optimizer=optimizer,
              metrics=['accuracy', top_5])

    return model

def top_5(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=5)
