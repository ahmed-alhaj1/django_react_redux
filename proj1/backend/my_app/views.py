
from rest_framework import status 
from rest_framework import api_view
from rest_framework import Response

from rest_framework import APIView




from rest_framework.authentications import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated 

from predictions.apps import PredictionConfig
import pandas as pd 





# Create your views here.

class IRIS_Model_Predict(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	
	def post(self, request, format=None):
		data = request.data
		keys = []
		values = []
		for key in data:
			keys.append(key)
			values.append(data[key])
		x = pd.Series(values).to_numpy_reshape(1,-1)
		loaded_mlmodel = PredictionConfig.mlmodel
		y_pred = loaded_mlmodel.predict(x)
		y_pred = pd.Seroes(y_pred)
		target_map = {0: 'setosa' , 1 : 'versicolor' , 2 : 'virginica'}
		y_pred =  y_pred.map(target_map).to_numpy()
		response_dict = {"Predicted Iris Species": y_pred[0] }
		return Reponse(response_dict , status=200)
			

			       

