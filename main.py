# importing the necessary dependencies
import sys
sys.path.append(r"c:\users\arpit\desktop\money-laundering-master\env\lib\site-packages")

import os
import pickle
import pandas
import pandas as pd
from flask import Flask, request, render_template
from flask import Response
from flask_cors import cross_origin

from trainingModel import trainModel

model_path = 'saved_model/DecisionTree/DecisionTree.pickle'
# model_path = 'EDA\PredictModel.pickle'
model = pickle.load(open(model_path, 'rb'))

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# initializing the flask app
app = Flask(__name__)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
# @cross_origin()
def PredictRoute():
    try:

        if request.json is not None:
            print('start 1')
            path = request.json['filepath']
            data = pandas.read_csv(path)
            y_predict = model.predict(data)
            final = pd.DataFrame(list(zip(y_predict)), columns=['Predictions'])
            path = "Prediction_Output_File/Predictions1.csv"
            final.to_csv("Prediction_Output_File/Predictions1.csv", index=False, header=True, mode='a+')

            return path

        elif request.form is not None:
            print('start 2')
            path = request.form['filepath']
            print('2')
            data = pandas.read_csv(path)
            print('3')
            y_predict = model.predict(data)
            print('4')
            data['isFraud'] = y_predict
            print('5')
            path = "Prediction_Output_File/Predictions1.csv"
            data.to_csv("Prediction_Output_File/Predictions1.csv", index=False, header=True, mode='a+')
            print('6')

            return  
        else:
            print('Nothing Matched')

    except ValueError as e:
        print(e)
        return Response("Error Occurred! %s" % e)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)


@app.route("/train", methods=['POST'])
@cross_origin()
def trainRouteClient():
    try:
        if request.json['folderPath'] is not None:  # folder-path is data
            path = request.json['folderPath']
            train_model_obj = trainModel()  # object initialization
            train_model_obj.trainingModel()  # training the model for the files in the table

    except ValueError:

        return Response("Error Occurred! %s" % ValueError)

    except KeyError:

        return Response("Error Occurred! %s" % KeyError)

    except Exception as e:

        return Response("Error Occurred! %s" % e)

    return Response("Training successfully done!!")


if __name__ == '__main__':
    app.run()
