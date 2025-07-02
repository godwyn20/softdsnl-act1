from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Load the Iris dataset and train the model when the server starts
iris = load_iris()
model = RandomForestClassifier()
model.fit(iris.data, iris.target)

class PredictIris(APIView):
    def post(self, request):
        try:
            data = request.data
            sepal_length = float(data.get('sepal_length'))
            sepal_width = float(data.get('sepal_width'))
            petal_length = float(data.get('petal_length'))
            petal_width = float(data.get('petal_width'))

            input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            prediction = model.predict(input_data)
            predicted_class = iris.target_names[prediction][0]

            return Response({'prediction': predicted_class})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)