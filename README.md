Created by: Paul A. Gureghian in July 2020. 

PyTorch LSTM Text Generation Demo.

Implemented via a PyTorch LSTM RNN network.

Programming language used: Python-3 

Machine Learning framework used: PyTorch

Python libraries used:  Numpy, Pandas

An LSTM model was created in 'model.py' file for converting word indexes to word vectors.

The dataset used was https://raw.githubusercontent.com/amoudgl/short-jokes-dataset/master/data/reddit-cleanjokes.csv

The dataset was loaded into PyTorch via a Dataset class defined in 'dataset.py' 

Training of the model is implemented in 'train.py' which has a 'train' function to train the model on the data
and a 'predict' function to make predictions and generate text.

The program shows the 'epochs', 'batch', 'loss', and 100 predicted words.

To run the program, first 'git' clone the repo, navigate to the project folder in terminal, and run the 'train.py' script like this:  

$ python3 train.py  or chmod 777 train.py then ./train.py