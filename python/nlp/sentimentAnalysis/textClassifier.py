'''
Sentiment analysis using louie ck jokes and scripts
'''

import os
import re
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
# Used by regression_model:
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

re_no_space = re.compile("[.;:!\'?,\"()\[\]]")
re_with_space = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

# Write to file.
def write_to_file (list_text, f) :

    for line in enumerate(list_text):
        f.write(line)
    print("### Writing to file complete ###")

# Load text, clean timestamps and rip sentences regex.
def text_preprocessor_loader (f) :
    text = []
    for line in enumerate(f):
        length = len(line)
        if line[length-1].isdigit():
            break
        text.append(line.strip())
    text =[re_no_space.sub("", line.lower()) for line in text]
    text =[re_with_space.sub(" ", line) for line in text]
    return text

def vectorization (train_data, test_data) :
    cv = CountVectorizer(binary=True)
    cv.fit(train_data)
    vectorized_train_data = cv.transform(train_data)
    vectorized_test_data = cv.transform(test_data)
    return [vectorized_test_data, vectorized_train_data]

def regression_model (data) :
    target = [1 if i < len(data)/2 else 0 for i in range(len(data))]

    X_train, X_val, y_train, y_val = train_test_split(
        data[0], target, train_size = 0.75
    )

    for c in [0.01, 0.05, 0.25, 0.5, 1]:
        
        lr = LogisticRegression(C=c)
        lr.fit(X_train, y_train)
        print ("Accuracy for C=%s: %s" 
            % (c, accuracy_score(y_val, lr.predict(X_val))))
    model = LogisticRegression(C=0.05)
    model.fit(data[1], target)
    print("Mode accuracy: %s"
        % accuracy_score(target, model.predict(data[0]))
    )

    return model

def main ():

    f = open("final_data_bundle", "a+")
    f.close()
    # NOTE Add an interface file.py that loops through inputs until -1 in given.
    # These inputs should be paths to files.

    liveAtTheComedyStore = 'LiveAtTheComedyStore/Louis.C.K..Live.At.The.Comedy.Store.2015.720p.WEBRip.x264-[YTS.AM].srt'
    louieHilarious = 'louieHilarious/Louis C.K. [2010] - Hilarious.srt'
    season1 = 'louieSeason1/allLouieSeason1'
    season2 = 'louieSeason2/allLouieSeason2'
    season3 = 'louieSeason3/allLouieSeason3'
    season4 = 'louieSeason4/allLouieSeason4'

    live1 = text_preprocessor_loader(liveAtTheComedyStore)
    live2 = text_preprocessor_loader(louieHilarious)
    se1 = text_preprocessor_loader(season1)
    se2 = text_preprocessor_loader(season2)
    se3 = text_preprocessor_loader(season3)
    se4 = text_preprocessor_loader(season4)

    final_bundle = [live1, live2, se1, se2, se3, se4]
    final_data = []

    for line in final_bundle:
        final_data.append()

    write_to_file(final_data, f)

    final_data_vectorized = vectorization(final_data[:((len(final_data) - 1)/2)], final_data[((len(final_data) - 1)/2):])
    model = regression_model(final_data_vectorized)

    # Print most positive and most negative words - top 5.
    feature_to_coef = {
        word: coef for word, coef in zip (
            CountVectorizer(binary=True).get_feature_names(), model.coef_[0]
        )
    }
    for top5_positive in sorted(
        feature_to_coef.items(), 
        key=lambda x: x[1], 
        reverse=True)[:5]:
        print (top5_positive)
        
    for top5_negative in sorted(
        feature_to_coef.items(), 
        key=lambda x: x[1])[:5]:
        print (top5_negative)

if __name__ == '__main__':
    main()