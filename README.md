# Multiclass Multilabel Prediction For StackOverflow Questions

**Data set** : https://www.kaggle.com/therajeshreddy/stackoverflow

**Objective** : Given text for Questions from StackoverFlow posts, predict tags associated with them.

This is a scaled down version of predecting only top 10 most occurring tags 

**Programming Language** : Python using nltk & Keras

**Model Architecture** : Deep Learning using Recurrent Neural Network (RNN)

**About Data Set** 

Dataset has text of questions, answers and thier corresponding tags from the Stack Overflow programming Q&A website.

This is organized as three files:

1. Questions contains the title, body, creation date, closed date (if applicable), score, and owner ID for all non-deleted Stack Overflow questions.

2. Tags contains the tags on each of these questions.

3. Answers contains the body, creation date, score, and owner ID for each of the answers to these questions. The ParentId column links back to the Questions table. *We don't use this file as we want to predict Tags given a question*

**Data Pre-Processing**

>Questions File
*Code* : Stackoverflow Clean Questions.ipynb

1. Read Questions File
2. Drop All columns except Id,Title and Body
3. Now the text in the Body column seem to have many html tags in the text. We use Regular Expressions and Clean the Body column text by removing the html tags
```python
import re 
def rem_html_tags(body):
    regex = re.compile('<.*?>')
    return re.sub(regex, '', body)
ques['Body'] = ques['Body'].apply(rem_html_tags)
```
4. Save the questions file for later use
```python
ques.to_csv('question_clean.csv',index=False)
```

>Tags File
*Code* : Stackoverflow Tags Map & Model.ipynb

1. Read Tags File
2. Identify top 10 Tags by count
```python
tagCount =  collections.Counter(list(df_tags['Tag'])).most_common(10)
print(tagCount)

[('javascript', 124155), ('java', 115212), ('c#', 101186), ('php', 98808), ('android', 90659), ('jquery', 78542), ('python', 64601), ('html', 58976), ('c++', 47591), ('ios', 47009)]
```

<img src="Images/top10_tags.JPG" width="600">

3. Manipulate the tags dataframe so that all the Tags for an ID are as a list in a row (grouped by Question ID)

```python
def add_tags(question_id):
    return tag_top10[tag_top10['Id'] == question_id['Id']].Tag.values

top10 = tag_top10.apply(add_tags, axis=1)
```


>Combine the Questions and Tags
*Code* : Stackoverflow Tags Map & Model.ipynb

Merge the Questions and Tags data frame by ID

```python
total=pd.merge(ques, top10_tags, on='Id')
```

Our Dataset would now have only Id, Title, Body & Tags

>Text Preprocessing
*Code* : Stackoverflow Tags Map & Model.ipynb

We will use nltk, preprocessing from Keras and sklearn to process the text data

*Tags preprocesing*
Use MultiLabelBinarizer from sklearn on the Class labels(Tags)
```python
from sklearn.preprocessing import MultiLabelBinarizer
multilabel_binarizer = MultiLabelBinarizer()
multilabel_binarizer.fit(total.Tags)
print(multilabel_binarizer.classes_)

array(['android', 'c#', 'c++', 'html', 'ios', 'java', 'javascript','jquery', 'php', 'python'], dtype=object)
```

*Title & Body Preprocessing*
1. Tokenize the words
2. Convert the tokenized words to sequences

**Model Building** 

Implemented a Hybrid model in TensorFlow using Keras as high level api. Architecture used is RNN. In this model first we train a model using the Title data, then train a model using the Body data. Outputs of both are concatenated and passed thorugh the dense layers before connecting to the output layer

*RNN Model* : The model first  uses GRU for the sequence data training with 2 GRU layers one for Title and other for Body. 

Each Layer has
  - 2 Conv2D layers (first layer with input of shape 240,240,3 (240x240 - Image Scale, 3 - RGB Scale))
  - 2 BatchNormalization layers [For Info click here](https://medium.com/deeper-learning/glossary-of-deep-learning-batch-normalisation-8266dcd2fa82)
  - 1 Dropout Layer of rate 30% 
  
*Model Compilattion with loss='categorical_crossentropy',metrics='accuracy' and optimizer='adam'*

*Call back for early stopping when test accuracy doesn't increase in 5 epochs*
```python
callback = [callbacks.EarlyStopping(monitor='val_accuracy',patience=5)]
```


```python

```



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
