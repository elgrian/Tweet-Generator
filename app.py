from flask import Flask
from flask import request
app = Flask(__name__)
import weighted_dictionary_histogram


@app.route('/')
def get_tweet():
    total_word = int(request.args.get('words'))
    complete_string = ""
    words = weighted_dictionary_histogram.file_open()
    new_histogram = weighted_dictionary_histogram.histogram(text)
    
    for _ in range(total_word):
        chosen_random_word = weighted_dictionary_histogram.random_word(new_histogram)
        complete_string = complete_string + " " + chosen_random_word
    return complete_string