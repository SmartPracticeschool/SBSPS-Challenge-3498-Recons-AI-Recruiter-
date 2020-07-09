from ideal_data import training_docs, training_doc_tokens, training_labels
from sklearn.naive_bayes import MultinomialNB
from preprocessing import preprocess_text
import csv


with open("users_response.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        test_text = float(row[0])


test_tokens = preprocess_text(test_text)

def create_features_dictionary(document_tokens):
  features_dictionary = {}
  index = 0
  for token in document_tokens:
    if token not in features_dictionary:
      features_dictionary[token] = index
      index += 1
  return features_dictionary

def tokens_to_bow_vector(document_tokens, features_dictionary):
  bow_vector = [0] * len(features_dictionary)
  for token in document_tokens:
    if token in features_dictionary:
      feature_index = features_dictionary[token]
      bow_vector[feature_index] += 1
  return bow_vector

bow_dictionary = create_features_dictionary(training_doc_tokens)
training_vectors = [tokens_to_bow_vector(training_doc, bow_dictionary) for training_doc in training_docs]
test_vectors = [tokens_to_bow_vector(test_tokens, bow_dictionary)]

classifier = MultinomialNB()
classifier.fit(training_vectors, training_labels)

predictions = classifier.predict(test_vectors)  

print("Accepted for walk-In interview" if predictions[0] == 0 else "Rejected")



            