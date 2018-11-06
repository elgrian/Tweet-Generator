from flask import Flask
from flask import request
app = Flask(__name__)
import weighted_dictionary_histogram as wdh


@app.route('/')
def get_tweet():
    total_word = request.args.get('words')
    complete_string = ""
    words = wdh.file_open()
    histo = wdh.histogram(text)
    
    for _ in range(int(total_word)):
        chosen_random_word = wdh.random_word(histo)
        complete_string = complete_string + " " + chosen_random_word
    return complete_string
    
# get_string()

# if __name__ == '__main__':
#     app.debug = True
#     app.run()