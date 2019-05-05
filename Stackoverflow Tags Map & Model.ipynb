{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
    "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['stackoverflow-clean-questions-file-v2', 'stackoverflow']\n"
     ]
    }
   ],
   "source": [
    "# This Python 3 environment comes with many helpful analytics libraries installed\n",
    "# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python\n",
    "# For example, here's several helpful packages to load in \n",
    "\n",
    "import numpy as np # linear algebra\n",
    "import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n",
    "\n",
    "# Input data files are available in the \"../input/\" directory.\n",
    "# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory\n",
    "\n",
    "import os\n",
    "print(os.listdir(\"../input\"))\n",
    "\n",
    "# Plotting Libs\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.cm as cm\n",
    "# magic function\n",
    "%matplotlib inline\n",
    "\n",
    "import collections"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "_cell_guid": "79c7e3d0-c299-4dcb-8224-4455121ee9b0",
    "_uuid": "d629ff2d2480ee46fbb7e2d37f6b5fab8052498a"
   },
   "outputs": [],
   "source": [
    "df_tags = pd.read_csv('../input/stackoverflow/Tags.csv', encoding='iso-8859-1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_tags(tagCount):\n",
    "    \n",
    "    x,y = zip(*tagCount)\n",
    "\n",
    "    colormap = plt.cm.gist_ncar #nipy_spectral, Set1,Paired  \n",
    "    colors = [colormap(i) for i in np.linspace(0, 0.8,50)]   \n",
    "\n",
    "    area = [i/4000 for i in list(y)]   # 0 to 15 point radiuses\n",
    "    plt.figure(figsize=(9,8))\n",
    "    plt.ylabel(\"Number of question associations\")\n",
    "    for i in range(len(y)):\n",
    "        plt.plot(i,y[i], marker='o', linestyle='',ms=area[i],label=x[i])\n",
    "\n",
    "    plt.legend(numpoints=1)\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('javascript', 124155), ('java', 115212), ('c#', 101186), ('php', 98808), ('android', 90659), ('jquery', 78542), ('python', 64601), ('html', 58976), ('c++', 47591), ('ios', 47009)]\n"
     ]
    },
    {
     "data": {
      "image/png": "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SQeNU045ha6urv06p6uri8WLF5dUkdqdQUiSdNCYN28eixYtajgMdXV1sWjRIp85VmEGIUnSQSMiOOOMMxoKQ4Mh6IwzzmhSdWpHrbqhoiRJpejo6ODNb34zxx13HLfffjurVq3a7enzc+fOZfHixfYEySAkSTo4zZ8/n/nz59Pb28uGDRvo6+uju7ubGTNmODFaTzMISZIOalOmTDH4aK+cIyRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkirLICRJkiqrJUEoIlZFxH0R8dOIWF60PS8ibomIh4ufU4v2iIgvRMSKiLg3Il4+5DrnFsc/HBHnDmk/obj+iuLcaP5vKUmS2l0re4R+OzNflpk9xf7HgVszcwFwa7EP8AZgQfE6D7gM6sEJuAg4CTgRuGgwPBXHfGDIeUvK/3UkSdJY005DY2cCVxTbVwBvHdJ+ZdbdARweETOA1wO3ZOZjmfk4cAuwpHhvcmbekZkJXDnkWpIkSU9rVRBK4J8j4u6IOK9om56ZG4rtjcD0YnsmsHbIueuKtuHa1+2hXZIk6Vk6W/S5p2Tm+og4CrglIh4c+mZmZkRk2UUUIew8gDlz5pT9cZIkqc20pEcoM9cXPzcD36I+x2dTMaxF8XNzcfh6YPaQ02cVbcO1z9pD+57quDwzezKzZ9q0aQf6a0mSpDGm6UEoIiZFxGGD28DpwM+B64HBlV/nAt8ptq8HzilWj50M9BZDaMuA0yNiajFJ+nRgWfHe1og4uVgtds6Qa0mSJD2tFUNj04FvFSvaO4GvZ+bNEXEXcHVEvB9YDbyjOP4m4I3ACuApYClAZj4WERcDdxXHfTozHyu2zwe+CkwEvlu8JEmSniXqC6vU09OTy5cvb3UZkiRpFETE3UNu0bNX7bR8XpIkqalatWpMkiTthye3PczaNV9hy5Zl7KptZ1zHRKZNez2z5yzl0EkLWl3emGUQkiSpjWXWeOihT/OrDddQq+0EdgFQ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\n",
      "text/plain": [
       "<Figure size 648x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "tagCount =  collections.Counter(list(df_tags['Tag'])).most_common(10)\n",
    "print(tagCount)\n",
    "plot_tags(tagCount)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "top10=['javascript','java','c#','php','android','jquery','python','html','c++','ios']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(826739, 2)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Id</th>\n",
       "      <th>Tag</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>260</td>\n",
       "      <td>c#</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>330</td>\n",
       "      <td>c++</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>650</td>\n",
       "      <td>c#</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>930</td>\n",
       "      <td>c#</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>1010</td>\n",
       "      <td>c#</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Id  Tag\n",
       "14   260   c#\n",
       "18   330  c++\n",
       "28   650   c#\n",
       "35   930   c#\n",
       "39  1010   c#"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tag_top10= df_tags[df_tags.Tag.isin(top10)]\n",
    "print (tag_top10.shape)\n",
    "tag_top10.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30798790    5\n",
       "31085960    5\n",
       "11648170    5\n",
       "35318730    5\n",
       "4009250     5\n",
       "30289880    5\n",
       "23267320    5\n",
       "35283570    5\n",
       "30991580    5\n",
       "23484760    5\n",
       "Name: Id, dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tag_top10['Id'].value_counts().head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Id</th>\n",
       "      <th>Tag</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>260</td>\n",
       "      <td>c#</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>330</td>\n",
       "      <td>c++</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>650</td>\n",
       "      <td>c#</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>930</td>\n",
       "      <td>c#</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>1010</td>\n",
       "      <td>c#</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Id  Tag\n",
       "14   260   c#\n",
       "18   330  c++\n",
       "28   650   c#\n",
       "35   930   c#\n",
       "39  1010   c#"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tag_top10.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_tags(question_id):\n",
    "    return tag_top10[tag_top10['Id'] == question_id['Id']].Tag.values\n",
    "\n",
    "top10 = tag_top10.apply(add_tags, axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(826739, (826739, 2))"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(top10),tag_top10.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Id</th>\n",
       "      <th>Tag</th>\n",
       "      <th>Tags</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>260</td>\n",
       "      <td>c#</td>\n",
       "      <td>[c#]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>330</td>\n",
       "      <td>c++</td>\n",
       "      <td>[c++]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>650</td>\n",
       "      <td>c#</td>\n",
       "      <td>[c#]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>930</td>\n",
       "      <td>c#</td>\n",
       "      <td>[c#]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>1010</td>\n",
       "      <td>c#</td>\n",
       "      <td>[c#]</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Id  Tag   Tags\n",
       "14   260   c#   [c#]\n",
       "18   330  c++  [c++]\n",
       "28   650   c#   [c#]\n",
       "35   930   c#   [c#]\n",
       "39  1010   c#   [c#]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tag_top10=pd.concat([tag_top10, top10.rename('Tags')], axis=1)\n",
    "tag_top10.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(826739, 2)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tag_top10.drop([\"Tag\"], axis=1, inplace=True)\n",
    "tag_top10.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "top10_tags=tag_top10.loc[tag_top10.astype(str).drop_duplicates().index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Id</th>\n",
       "      <th>Title</th>\n",
       "      <th>Body</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>80</td>\n",
       "      <td>SQLStatement.execute() - multiple queries in o...</td>\n",
       "      <td>I've written a database generation script in S...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>90</td>\n",
       "      <td>Good branching and merging tutorials for Torto...</td>\n",
       "      <td>Are there any really good tutorials explaining...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>120</td>\n",
       "      <td>ASP.NET Site Maps</td>\n",
       "      <td>Has anyone got experience creating SQL-based A...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>180</td>\n",
       "      <td>Function for creating color wheels</td>\n",
       "      <td>This is something I've pseudo-solved many time...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>260</td>\n",
       "      <td>Adding scripting functionality to .NET applica...</td>\n",
       "      <td>I have a little game written in C#. It uses a ...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Id                        ...                                                                       Body\n",
       "0   80                        ...                          I've written a database generation script in S...\n",
       "1   90                        ...                          Are there any really good tutorials explaining...\n",
       "2  120                        ...                          Has anyone got experience creating SQL-based A...\n",
       "3  180                        ...                          This is something I've pseudo-solved many time...\n",
       "4  260                        ...                          I have a little game written in C#. It uses a ...\n",
       "\n",
       "[5 rows x 3 columns]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ques = pd.read_csv('../input/stackoverflow-clean-questions-file-v2/question_clean.csv', encoding='iso-8859-1')\n",
    "ques.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(706336, 4)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Id</th>\n",
       "      <th>Title</th>\n",
       "      <th>Body</th>\n",
       "      <th>Tags</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>260</td>\n",
       "      <td>Adding scripting functionality to .NET applica...</td>\n",
       "      <td>I have a little game written in C#. It uses a ...</td>\n",
       "      <td>[c#]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>330</td>\n",
       "      <td>Should I use nested classes in this case?</td>\n",
       "      <td>I am working on a collection of classes used f...</td>\n",
       "      <td>[c++]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>650</td>\n",
       "      <td>Automatically update version number</td>\n",
       "      <td>I would like the version property of my applic...</td>\n",
       "      <td>[c#]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>930</td>\n",
       "      <td>How do I connect to a database and loop over a...</td>\n",
       "      <td>What's the simplest way to connect and query a...</td>\n",
       "      <td>[c#]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1010</td>\n",
       "      <td>How to get the value of built, encoded ViewState?</td>\n",
       "      <td>I need to grab the base64-encoded representati...</td>\n",
       "      <td>[c#]</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Id  ...     Tags\n",
       "0   260  ...     [c#]\n",
       "1   330  ...    [c++]\n",
       "2   650  ...     [c#]\n",
       "3   930  ...     [c#]\n",
       "4  1010  ...     [c#]\n",
       "\n",
       "[5 rows x 4 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "total=pd.merge(ques, top10_tags, on='Id')\n",
    "print(total.shape)\n",
    "total.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Using TensorFlow backend.\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import MultiLabelBinarizer\n",
    "from nltk import word_tokenize\n",
    "from keras.preprocessing.text import Tokenizer\n",
    "from keras.preprocessing import sequence\n",
    "from keras.layers import LSTM, Activation, Dense, Dropout, Input, Embedding, BatchNormalization, GRU ,concatenate\n",
    "from keras.models import Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['android', 'c#', 'c++', 'html', 'ios', 'java', 'javascript',\n",
       "       'jquery', 'php', 'python'], dtype=object)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "multilabel_binarizer = MultiLabelBinarizer()\n",
    "multilabel_binarizer.fit(total.Tags)\n",
    "labels = multilabel_binarizer.classes_\n",
    "labels"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "train,test=train_test_split(total[:550000],test_size=0.25,random_state=24)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((412500, 4), (137500, 4))"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.shape,test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train_t=train['Title']\n",
    "X_train_b=train['Body']\n",
    "y_train=multilabel_binarizer.transform(train['Tags'])\n",
    "X_test_t=test['Title']\n",
    "X_test_b=test['Body']\n",
    "y_test=multilabel_binarizer.transform(test['Tags'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "59"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sent_lens_t=[]\n",
    "for sent in train['Title']:\n",
    "    sent_lens_t.append(len(word_tokenize(sent)))\n",
    "max(sent_lens_t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "18.0"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.quantile(sent_lens_t,0.97)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "max_len_t = 18\n",
    "tok = Tokenizer(char_level=False,split=' ')\n",
    "tok.fit_on_texts(X_train_t)\n",
    "sequences_train_t = tok.texts_to_sequences(X_train_t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "68969"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vocab_len_t=len(tok.index_word.keys())\n",
    "vocab_len_t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[    0,     0,     0, ...,     1,   957,   197],\n",
       "       [    0,     0,     0, ...,  9081,    45,   533],\n",
       "       [    0,     0,     0, ...,   147,     8,   230],\n",
       "       ...,\n",
       "       [    0,     0,     0, ...,    10,    71,  2985],\n",
       "       [    0,     0,     0, ...,     2,    18,    75],\n",
       "       [    0,     0,     0, ..., 11009,   809,   267]], dtype=int32)"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sequences_matrix_train_t = sequence.pad_sequences(sequences_train_t,maxlen=max_len_t)\n",
    "sequences_matrix_train_t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "sequences_test_t = tok.texts_to_sequences(X_test_t)\n",
    "sequences_matrix_test_t = sequence.pad_sequences(sequences_test_t,maxlen=max_len_t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((412500, 18), (137500, 18), (412500, 10), (137500, 10))"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sequences_matrix_train_t.shape,sequences_matrix_test_t.shape,y_train.shape,y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20853"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sent_lens_b=[]\n",
    "for sent in train['Body']:\n",
    "    sent_lens_b.append(len(word_tokenize(sent)))\n",
    "max(sent_lens_b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "575.0"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.quantile(sent_lens_b,0.90)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "max_len_b = 600\n",
    "tok = Tokenizer(char_level=False,split=' ')\n",
    "tok.fit_on_texts(X_train_b)\n",
    "sequences_train_b = tok.texts_to_sequences(X_train_b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1292018"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vocab_len_b =len(tok.index_word.keys())\n",
    "vocab_len_b "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[   0,    0,    0, ...,   51, 2082,   91],\n",
       "       [   0,    0,    0, ..., 1408,  203,  825],\n",
       "       [   0,    0,    0, ...,   34,   51,   83],\n",
       "       ...,\n",
       "       [   0,    0,    0, ...,   20,   68,  687],\n",
       "       [   0,    0,    0, ...,  187,   58,   10],\n",
       "       [   0,    0,    0, ...,  194,  197,   10]], dtype=int32)"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sequences_matrix_train_b = sequence.pad_sequences(sequences_train_b,maxlen=max_len_b)\n",
    "sequences_matrix_train_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "sequences_test_b = tok.texts_to_sequences(X_test_b)\n",
    "sequences_matrix_test_b = sequence.pad_sequences(sequences_test_b,maxlen=max_len_b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((412500, 18), (412500, 600), (412500, 10))"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sequences_matrix_train_t.shape,sequences_matrix_train_b.shape,y_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((137500, 18), (137500, 600), (137500, 10))"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sequences_matrix_test_t.shape,sequences_matrix_test_b.shape,y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "def RNN():\n",
    "    # Title Only\n",
    "    title_input = Input(name='title_input',shape=[max_len_t])\n",
    "    title_Embed = Embedding(vocab_len_t+1,2000,input_length=max_len_t,mask_zero=True,name='title_Embed')(title_input)\n",
    "    gru_out_t = GRU(300)(title_Embed)\n",
    "    # auxiliary output to tune GRU weights smoothly \n",
    "    auxiliary_output = Dense(10, activation='sigmoid', name='aux_output')(gru_out_t)   \n",
    "    \n",
    "    # Body Only\n",
    "    body_input = Input(name='body_input',shape=[max_len_b]) \n",
    "    body_Embed = Embedding(vocab_len_b+1,170,input_length=max_len_b,mask_zero=True,name='body_Embed')(body_input)\n",
    "    gru_out_b = GRU(200)(body_Embed)\n",
    "    \n",
    "    # combined with GRU output\n",
    "    com = concatenate([gru_out_t, gru_out_b])\n",
    "    \n",
    "    # now the combined data is being fed to dense layers\n",
    "    dense1 = Dense(400,activation='relu')(com)\n",
    "    dp1 = Dropout(0.5)(dense1)\n",
    "    bn = BatchNormalization()(dp1) \n",
    "    dense2 = Dense(150,activation='relu')(bn)\n",
    "    \n",
    "    main_output = Dense(10, activation='sigmoid', name='main_output')(dense2)\n",
    "    \n",
    "    model = Model(inputs=[title_input, body_input],outputs=[main_output, auxiliary_output])\n",
    "    return model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:From /opt/conda/lib/python3.6/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.\n",
      "Instructions for updating:\n",
      "Colocations handled automatically by placer.\n",
      "WARNING:tensorflow:From /opt/conda/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.\n",
      "Instructions for updating:\n",
      "Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.\n",
      "__________________________________________________________________________________________________\n",
      "Layer (type)                    Output Shape         Param #     Connected to                     \n",
      "==================================================================================================\n",
      "title_input (InputLayer)        (None, 18)           0                                            \n",
      "__________________________________________________________________________________________________\n",
      "body_input (InputLayer)         (None, 600)          0                                            \n",
      "__________________________________________________________________________________________________\n",
      "title_Embed (Embedding)         (None, 18, 2000)     137940000   title_input[0][0]                \n",
      "__________________________________________________________________________________________________\n",
      "body_Embed (Embedding)          (None, 600, 170)     219643230   body_input[0][0]                 \n",
      "__________________________________________________________________________________________________\n",
      "gru_1 (GRU)                     (None, 300)          2070900     title_Embed[0][0]                \n",
      "__________________________________________________________________________________________________\n",
      "gru_2 (GRU)                     (None, 200)          222600      body_Embed[0][0]                 \n",
      "__________________________________________________________________________________________________\n",
      "concatenate_1 (Concatenate)     (None, 500)          0           gru_1[0][0]                      \n",
      "                                                                 gru_2[0][0]                      \n",
      "__________________________________________________________________________________________________\n",
      "dense_1 (Dense)                 (None, 400)          200400      concatenate_1[0][0]              \n",
      "__________________________________________________________________________________________________\n",
      "dropout_1 (Dropout)             (None, 400)          0           dense_1[0][0]                    \n",
      "__________________________________________________________________________________________________\n",
      "batch_normalization_1 (BatchNor (None, 400)          1600        dropout_1[0][0]                  \n",
      "__________________________________________________________________________________________________\n",
      "dense_2 (Dense)                 (None, 150)          60150       batch_normalization_1[0][0]      \n",
      "__________________________________________________________________________________________________\n",
      "main_output (Dense)             (None, 10)           1510        dense_2[0][0]                    \n",
      "__________________________________________________________________________________________________\n",
      "aux_output (Dense)              (None, 10)           3010        gru_1[0][0]                      \n",
      "==================================================================================================\n",
      "Total params: 360,143,400\n",
      "Trainable params: 360,142,600\n",
      "Non-trainable params: 800\n",
      "__________________________________________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "model = RNN()\n",
    "model.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.compile(optimizer='adam',loss={'main_output': 'categorical_crossentropy', 'aux_output': 'categorical_crossentropy'},\n",
    "              metrics=['accuracy'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:From /opt/conda/lib/python3.6/site-packages/tensorflow/python/ops/math_ops.py:3066: to_int32 (from tensorflow.python.ops.math_ops) is deprecated and will be removed in a future version.\n",
      "Instructions for updating:\n",
      "Use tf.cast instead.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.6/site-packages/tensorflow/python/ops/gradients_impl.py:107: UserWarning: Converting sparse IndexedSlices to a dense Tensor with 137940000 elements. This may consume a large amount of memory.\n",
      "  num_elements)\n",
      "/opt/conda/lib/python3.6/site-packages/tensorflow/python/ops/gradients_impl.py:107: UserWarning: Converting sparse IndexedSlices to a dense Tensor with 219643230 elements. This may consume a large amount of memory.\n",
      "  num_elements)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train on 412500 samples, validate on 137500 samples\n",
      "Epoch 1/5\n",
      "412500/412500 [==============================] - 819s 2ms/step - loss: 2.3168 - main_output_loss: 1.0405 - aux_output_loss: 1.2763 - main_output_acc: 0.7285 - aux_output_acc: 0.6705 - val_loss: 1.7714 - val_main_output_loss: 0.7258 - val_aux_output_loss: 1.0456 - val_main_output_acc: 0.8254 - val_aux_output_acc: 0.7285\n",
      "Epoch 2/5\n",
      "412500/412500 [==============================] - 797s 2ms/step - loss: 1.5874 - main_output_loss: 0.6490 - aux_output_loss: 0.9384 - main_output_acc: 0.8443 - aux_output_acc: 0.7582 - val_loss: 1.7043 - val_main_output_loss: 0.6581 - val_aux_output_loss: 1.0462 - val_main_output_acc: 0.8379 - val_aux_output_acc: 0.7286\n",
      "Epoch 3/5\n",
      "412500/412500 [==============================] - 797s 2ms/step - loss: 1.3994 - main_output_loss: 0.5472 - aux_output_loss: 0.8522 - main_output_acc: 0.8650 - aux_output_acc: 0.7774 - val_loss: 1.7369 - val_main_output_loss: 0.6660 - val_aux_output_loss: 1.0708 - val_main_output_acc: 0.8364 - val_aux_output_acc: 0.7263\n",
      "Epoch 4/5\n",
      "412500/412500 [==============================] - 798s 2ms/step - loss: 1.2719 - main_output_loss: 0.4735 - aux_output_loss: 0.7984 - main_output_acc: 0.8774 - aux_output_acc: 0.7885 - val_loss: 1.7988 - val_main_output_loss: 0.6976 - val_aux_output_loss: 1.1012 - val_main_output_acc: 0.8369 - val_aux_output_acc: 0.7240\n",
      "Epoch 5/5\n",
      "412500/412500 [==============================] - 797s 2ms/step - loss: 1.1665 - main_output_loss: 0.4110 - aux_output_loss: 0.7555 - main_output_acc: 0.8868 - aux_output_acc: 0.7976 - val_loss: 1.9099 - val_main_output_loss: 0.7671 - val_aux_output_loss: 1.1428 - val_main_output_acc: 0.8307 - val_aux_output_acc: 0.7237\n"
     ]
    }
   ],
   "source": [
    "results=model.fit({'title_input': sequences_matrix_train_t, 'body_input': sequences_matrix_train_b},\n",
    "          {'main_output': y_train, 'aux_output': y_train},\n",
    "          validation_data=[{'title_input': sequences_matrix_test_t, 'body_input': sequences_matrix_test_b},\n",
    "          {'main_output': y_test, 'aux_output': y_test}],\n",
    "          epochs=5, batch_size=800)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "137500/137500 [==============================] - 1270s 9ms/step\n"
     ]
    }
   ],
   "source": [
    "(predicted_main, predicted_aux)=model.predict({'title_input': sequences_matrix_test_t, 'body_input': sequences_matrix_test_b},verbose=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import classification_report,f1_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8424636536796537\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.6/site-packages/sklearn/metrics/classification.py:1143: UndefinedMetricWarning: F-score is ill-defined and being set to 0.0 in samples with no predicted labels.\n",
      "  'precision', 'predicted', average, warn_for)\n"
     ]
    }
   ],
   "source": [
    "print(f1_score(y_test,predicted_main>.55,average='samples'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.97      0.93      0.95     17054\n",
      "           1       0.92      0.84      0.88     20681\n",
      "           2       0.92      0.81      0.86      9700\n",
      "           3       0.69      0.53      0.60     11304\n",
      "           4       0.96      0.91      0.94      8897\n",
      "           5       0.91      0.80      0.85     22472\n",
      "           6       0.82      0.72      0.76     22938\n",
      "           7       0.81      0.83      0.82     16150\n",
      "           8       0.92      0.90      0.91     19659\n",
      "           9       0.97      0.92      0.95     11576\n",
      "\n",
      "   micro avg       0.89      0.82      0.85    160431\n",
      "   macro avg       0.89      0.82      0.85    160431\n",
      "weighted avg       0.89      0.82      0.85    160431\n",
      " samples avg       0.86      0.85      0.84    160431\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.6/site-packages/sklearn/metrics/classification.py:1143: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in samples with no predicted labels.\n",
      "  'precision', 'predicted', average, warn_for)\n"
     ]
    }
   ],
   "source": [
    "print(classification_report(y_test,predicted_main>.55))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Id                                                16470700\n",
       "Title    NetworkOnMainThreadException- Have tried makin...\n",
       "Body     I've been trying to get this to work for a whi...\n",
       "Tags                                       [java, android]\n",
       "Name: 250148, dtype: object"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test.iloc[24]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1.  , 0.  , 0.  , 0.  , 0.  , 0.84, 0.  , 0.  , 0.  , 0.  ],\n",
       "      dtype=float32)"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "predicted_main[24].round(decimals = 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['android', 'c#', 'c++', 'html', 'ios', 'java', 'javascript',\n",
       "       'jquery', 'php', 'python'], dtype=object)"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "labels"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.save('./stackoverflow_tags.h5')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
