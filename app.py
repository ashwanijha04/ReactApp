import json
from flask import Flask, request, Response, jsonify
import sys
import pickle
import pandas as pd
import numpy as np
#sys.path.insert(0, '/Users/ashwajha/Desktop/ReactApp')

app = Flask(__name__)


import pickle
import pandas as pd
import numpy as np
import keras

pickle_in = open("/Users/ashwajha/Desktop/ReactApp/resRnet/finalized_model.sav","rb")



def ResNetAlgo(sequence):

    df = pd.read_csv("/users/ashwajha/Downloads/FeatureVectors.csv")

    model = pickle.load(pickle_in)

    seq = {}
    seq= df.sample()
    classes = []
    classes.append("Alpha Helix")
    classes.append("Random Coil")
    classes.append("Extended Strand")
    #print(classes[0])

    #seq = [0.32467532,0.37662336,0.2987013,0.3181818,0.37012988,0.3116883,0.3181818,0.2792208,0.4025974,0.29220778,0.3961039,0.3116883,0.14285715,0.09090909,0.11038961,0.16233766,0.12337662,0.103896104,0.077922076,0.14285715]
    seq1 = np.array(seq)
    seq1 = seq1.reshape(1,-1)
    #print (seq1)
    result = model.predict(seq1)
    idx = np.argmax(result)
    print(result)


    return (classes[idx])




notes = {

}

#def findString(s):
#    str = s

@app.route('/predict', methods=['GET', 'POST'])
def serve():
    i=0
    if request.method == 'POST' and request.is_json:
        new_note = request.get_json()['note']
        new_note_id = len(notes)
        notes[i] = (new_note)
        i = i + 1
        print(new_note)

    return Response(

        json.dumps(notes),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )

"""@app.route('/api/v1/notes', methods=['POST'])
def serve_again():
    return Response(

        json.dumps({
            "Accuracy": accuracy,
            "sequence": str
            }
        ),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )"""


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True)
