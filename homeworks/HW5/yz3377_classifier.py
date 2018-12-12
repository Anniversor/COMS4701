import sys
import string
import math


class NbClassifier(object):
    """
    A Naive Bayes classifier object has three parameters, all of which are populated during initialization:
    - a set of all possible attribute types
    - a dictionary of the probabilities P(Y), labels as keys and probabilities as values
    - a dictionary of the probabilities P(F|Y), with (feature, label) pairs as keys and probabilities as values
    """

    def __init__(self, training_filename, stopword_file):
        self.attribute_types = set()
        self.label_prior = {}
        self.word_given_label = {}

        self.collect_attribute_types(training_filename)
        if stopword_file is not None:
            self.remove_stopwords(stopword_file)
        self.train(training_filename)

    """
    A helper function to transform a string into a list of word strings.
    You should not need to modify this unless you want to improve your classifier in the extra credit portion.
    """

    def extract_words(self, text):
        no_punct_text = "".join([x for x in text.lower() if not x in string.punctuation])
        return [word for word in no_punct_text.split()]

    """
    Given a stopword_file, read in all stop words and remove them from self.attribute_types
    Implement this for extra credit.
    """

    def remove_stopwords(self, stopword_file):
        file = open(stopword_file, "r", encoding="UTF-8")
        lines = file.readlines()
        stop = set()
        for line in lines:
            stop.add(line.strip('\n'))
        # for word in self.attribute_types:
        #     if word.isdigit():
        #         stop.add(word)
        self.attribute_types = self.attribute_types.difference(stop)
        pass

    """
    Given a training datafile, add all features that appear at least m times to self.attribute_types
    """

    def collect_attribute_types(self, training_filename, m=1):
        # self.attribute_types = set()
        d = {}
        with open(training_filename, 'r', encoding="UTF-8") as fileReader:
            for line in fileReader:
                text = line.split('\t')[1]
                words = self.extract_words(text)
                for word in words:
                    if word in d.keys():
                        d[word] += 1
                    else:
                        d[word] = 1

        for k, v in d.items():
            if v >= m:
                self.attribute_types.add(k)
        pass

    """
    Given a training datafile, estimate the model probability parameters P(Y) and P(F|Y).
    Estimates should be smoothed using the smoothing parameter k.
    """

    def train(self, training_filename, k=0.2):
        # self.label_prior = {}
        # self.word_given_label = {}
        fileReader = open(training_filename, 'r', encoding="UTF-8")
        lines = fileReader.readlines()
        for line in lines:
            label = line.split("\t")[0]
            self.label_prior[label] = 0

        for label in self.label_prior.keys():
            for word in self.attribute_types:
                self.word_given_label[(word, label)] = 0

        for line in lines:
            label = line.split("\t")[0]  # label
            text = line.split("\t")[1]
            words = self.extract_words(text)
            self.label_prior[label] += 1
            for word in words:
                if word in self.attribute_types:
                    self.word_given_label[(word, label)] += 1

        for word_label, value in self.word_given_label.items():
            label = word_label[1]
            total_y = self.label_prior[label]
            self.word_given_label[word_label] = (value + k) / (total_y + k * len(self.attribute_types))

        for label, value in self.label_prior.items():
            self.label_prior[label] = value / len(lines)
        pass

    """
    Given a piece of text, return a relative belief distribution over all possible labels.
    The return value should be a dictionary with labels as keys and relative beliefs as values.
    The probabilities need not be normalized and may be expressed as log probabilities. 
    """

    def predict(self, text):
        beliefs = {}
        for label in self.label_prior.keys():
            beliefs[label] = math.log(self.label_prior[label])
        words = self.extract_words(text)
        for label in self.label_prior.keys():
            for word in words:
                if (word, label) in self.word_given_label.keys():
                    beliefs[label] += math.log(self.word_given_label[(word, label)])
        return beliefs

    """
    Given a datafile, classify all lines using predict() and return the accuracy as the fraction classified correctly.
    """

    def evaluate(self, test_filename):
        file = open(test_filename, 'r', encoding="UTF-8")
        lines = file.readlines()
        false = 0
        for line in lines:
            true_label = line.split("\t")[0]  # correct label
            text = line.split("\t")[1]
            beliefs = self.predict(text)
            value_true_label = beliefs[true_label]
            for label in beliefs.keys():
                if label != true_label and beliefs[label] > value_true_label:
                    false += 1
                    break
        return 1 - false / len(lines)


if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("\nusage: ./hmm.py [training data file] [test or dev data file] [(optional) stopword file]")
        exit(0)
    elif len(sys.argv) == 3:
        classifier = NbClassifier(sys.argv[1], None)
    else:
        classifier = NbClassifier(sys.argv[1], sys.argv[3])
    print(classifier.evaluate(sys.argv[1]))
    print(classifier.evaluate(sys.argv[2]))
