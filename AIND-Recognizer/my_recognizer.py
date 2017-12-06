import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    # TODO implement the recognizer
    # return probabilities, guesses
    # Loop over values in the test set of words
    for X_test, lengths_test in test_set.get_all_Xlengths().values():
        best_word_score = float('-inf')
        word_scores = {}
        word_guess = None
        # Loop through items in the trained model
        for word, model in models.items():
            try:
                # Compute logL using the selected model and test set features
                logL_score = model.score(X_test, lengths_test)
                # Set the word_score for the specific word to the calculated logL
                word_scores[word] = logL_score
                if logL_score > best_word_score:
                    best_word_score = logL_score
                    word_guess = word
            except:
                word_scores[word] = float("-inf")

        # Update probabilities list with word scores
        probabilities.append(word_scores)
        # Update guesses list with word guesses
        guesses.append(word_guess)
    return(probabilities, guesses)
