# AnalogySolver
![GitHub](https://img.shields.io/github/license/kazifarhan199/AnalogySolver)

An analogy solver is a web-based application that utilizes Natural Language Processing (NLP) techniques, specifically word embeddings, to solve analogies. Word embeddings are a way to represent words in a high-dimensional space, where semantically similar words are located close to one another. These embeddings are often pre-trained on a large corpus of text data and are used to represent words in a numerical form, making them amenable to mathematical operations. By using this technology, the analogy solver is able to understand the relationships between words and use that knowledge to solve analogies, such as "king is to queen as man is to ____." 


<img src="./assets/example.png" alt="phone DesktopExample" height="300"/> <img src="./assets/phone_example.png" alt="phone example" height="300"/>
<img src="./assets/phone_example2.png" alt="phone example" height="300"/>

We are utilizing a pre-trained GloVe model in this application. You can find more information about this model by visiting the Stanford NLP Group website at https://nlp.stanford.edu/projects/glove/. GloVe, which stands for 'Global Vectors for Word Representation', was developed by researchers at Stanford University in 2014. It is trained on vast amounts of text data through a method called co-occurrence matrix factorization. This pre-trained model can be fine-tuned for various NLP tasks, such as sentiment analysis, named entity recognition, and machine translation. It is a widely used and highly respected model in the NLP community, often serving as a starting point for a variety of NLP tasks, with many achieving good performance without the need for extensive fine-tuning.


# DataSet

We are utilizing the GloVe dataset, specifically the version "glove.6B.100d", in this project. This dataset, which stands for "Global Vectors for Word Representation," is trained on a corpus of 6 billion tokens and has 100-dimensional embeddings for each word. The embeddings in this dataset are pre-trained on a large amount of text data, and can be used as a starting point for a variety of natural language processing tasks. The dataset is publicly available for download at the following link: https://nlp.stanford.edu/projects/glove/ You can find more detailed information about this dataset on the GloVe website, where you will find other version of dataset which can be used for different NLP tasks

# Setup

1. Download glove
Download glove.6B.zip from [https://nlp.stanford.edu/projects/glove/](https://nlp.stanford.edu/projects/glove/) unzip it.
Move the 'glove.6B.100d' file to the project folder.

2. Create a virtualenv and activate it 
```
python3 -m virtualenv env
```
```
source env/bin/activate
```

3. Install the dependencies
```
pip install -r requirements.txt
```

4. Run the project
```
python manage.py runserver
```

5. Go to `localhost:8000` and have fun!

