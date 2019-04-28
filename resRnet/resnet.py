import pickle
import pandas as pd
import numpy as np
import keras

def ResNetAlgo(sequence):

	pickle_in = open("finalized_model.sav","rb")
	model = pickle.load(pickle_in)
	df = pd.read_csv("/users/autkarsh/Downloads/FeatureVectors.csv")


	seq = {}
	seq= df.sample()
	#seq = [0.32467532,0.37662336,0.2987013,0.3181818,0.37012988,0.3116883,0.3181818,0.2792208,0.4025974,0.29220778,0.3961039,0.3116883,0.14285715,0.09090909,0.11038961,0.16233766,0.12337662,0.103896104,0.077922076,0.14285715]
	seq1 = np.array(seq)
	seq1 = seq1.reshape(1,-1)
	#print (seq1)
	result = model.predict(seq1)
	return result
ResNetAlgo("asdasdad")
