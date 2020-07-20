#!/usr/bin/env python3

# import libraries
import torch
import pandas as pd 
from collections import Counter

# Define Dataset class 
class Dataset(torch.utils.data.Dataset):

    def __init__(self, args):

        self.args = args
        self.words = self.load_words()
        self.unique_words = self.get_unique_words()

        self.index_to_word = {index: word for index, word in enumerate(self.unique_words)}
        self.word_to_index = {word: index for index, word in enumerate(self.unique_words)}

        self.words_indexes = [self.word_to_index[w] for w in self.words]

    def load_words(self):

        train_df = pd.read_csv('data/jokes.csv')
        text = train_df['Joke'].str.cat(sep =  ' ')

        return text.split(' ')

    def get_unique_words(self):

        word_counts = Counter(self.words)

        return sorted(word_counts, key = word_counts.get, reverse = True)

    def __len__(self):

        return len(self.words_indexes) - self.args.sequence_length

    def __getitem__(self, index):

        return (torch.tensor(self.words_indexes[index:index + self.args.sequence_length]),
                torch.tensor(self.words_indexes[index + 1:index + self.args.sequence_length + 1]))                                                                                        