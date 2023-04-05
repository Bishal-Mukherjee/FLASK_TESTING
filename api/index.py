from flask import Flask, app, request, json
# from ml.model import *
app = Flask(__name__)


@app.route('/')
def index():
    return {'message': 'server working'}


# @app.route('/', methods=['POST'])
# def predict():
#     reqbody = json.loads(request.data)
#     symptoms = []

#     if len(reqbody['symptoms']) == 0:
#         return {'message': 'no symptoms provided'}

#     for symptom in reqbody['symptoms']:
#         try:
#             if(symptom.index(" ")):
#                 symptoms.append(symptom.replace(" ", '_'))
#         except:
#             symptoms.append(symptom)

#     predictedDiease = NaiveBayes(symptoms)

#     return {'predictedDiease': predictedDiease}


if __name__ == "__main__":
    app.run()
