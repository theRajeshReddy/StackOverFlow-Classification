# Multiclass Multilabel Prediction For StackOverflow Questions

**Data set** : https://www.kaggle.com/therajeshreddy/stackoverflow

**Objective** : Given text for Questions, predict tags associated with them.

This is a scaled down version of predecting only top 10 most occurring tags 

**Data Preparation** 

>Questions File
*Code* : Stackoverflow Clean Questions.ipynb

1. Read Questions File
2. Drop All columns except Id,Title and Body
3. Use Regular Expressions and Clean the Body column text by removing the html tags
4. Combine Title and Body columns 
5. Save the questions file for later use

>Tags File
*Code* : Stackoverflow Tags Map & Model.ipynb

1. Read Tags File
2. Manipulate the tags dataframe so that all the Tags for an ID are as a list in a row

>Combine the Questions and Tags
*Code* : Stackoverflow Tags Map & Model.ipynb

**Model Building** 

*Code* : Distracted_Driver_MultiAction_Classification.ipynb

Implimented in Keras using RNN(GRU) architecture 

1. Use MultiLabelBinarizer on our Target Class Tags
2. Tokenize the Content(questions+description) and convert them to Sequence
3. Pad Sequences with Zero
4. Model Architecture - Embedding Layer(reduced the output due to hardware limitation) + GRU + Combinaation of Dense, Dropout and BatchNormalization Layers + Softmax Output layer
5. Model Compilatation with optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']
6. Batch Generator so pass the imput to the model in batches. Batch size = 800
7. Fit/Train the Model 
8. Save Model for later use
