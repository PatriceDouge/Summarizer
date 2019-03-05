import argparse
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

def main():
    args = parse_arguments()

    content = read_file(args.filepath)
    content = data_clean(content) #cleaning data using our func

    sentence_tokens, word_tokens = tokenize_content(content)

    return sentence_tokens

    return word_tokens

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='File name of text to summarize')
    parser.add_argument('-l', '--length', default=4, help='Number of sentences to return')
    args = parser.parse_args()

    return args

#reads file and returns error if file not found or cant be read
def read_file(path):
    try: 
        with open(path, 'r') as file:
            return file.read()

    except IOError as e:
         return "Error: File ({}) could not be read".format(path)

#cleaning up white space thats in data
def data_clean(data):
    replace = {
        ord('\f') : ' ',
        ord('\t') : ' ', 
        ord('\n') : ' ', 
        ord('\r') : None
    }
    return data.translate(replace)

#func to return all unique words thats not in stop words 
def tokenize_content(content):
    stop_words = set(stopwords.words('english') + list(punctuation)) #stop words like and, or that would have an inpact on final scoing 
    words = word_tokenize(content.lower())

    return [
        sent_tokenize(content),
        [word for word in words if word not in stop_words]
    ]

    
if __name__ == "__main__":
    print(main())