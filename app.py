from flask import Flask, request, render_template,redirect,url_for
from flask_cors import cross_origin
import pickle
import numpy as np
import pandas as pd
import warnings

app = Flask(__name__)
app.config['DEBUG']=True


# @app.route('/',methods=['GET'])
# def home():
#     return render_template('ff.html')

# model = pickle.load(open("flight_rf.pkl", "rb"))
model = pickle.load(open("flight_rf.pkl", "rb"))
@app.route("/")
@cross_origin()
def home():
    return render_template("ff.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
#----------------------------------------------------------------
def predict():
    if request.method == "POST":
        Destination = request.form["Destination"]
        Total_stops = int(request.form["Total_Stops"])
        Source = request.form["Source"]
        Airline=request.form['Airline']
        date_dep = request.form["Departure_Date"]
        date_arr = request.form["Arrival_Date"]
        
        
        

        Journey_day = int(pd.to_datetime(date_dep).day)
        Journey_month = int(pd.to_datetime(date_dep).month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep).hour)
        Dep_min = int(pd.to_datetime(date_dep).minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        #date_arr = request.form["Arrival_Date"]
        Arrival_hour = int(pd.to_datetime(date_arr).hour)
        Arrival_min = int(pd.to_datetime(date_arr).minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        #Total_stops = int(request.form["stops"])  
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        #Airline=request.form['Airline'] 
        if(Airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            Air_Asia = 0

        elif (Airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            Air_Asia = 0

        elif (Airline=='Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            Air_Asia = 0
            
        elif (Airline=='Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            Air_Asia = 0
            
        elif (Airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            Air_Asia = 0
            
        elif (Airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            Air_Asia = 0

        elif (Airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            Air_Asia = 0

        elif (Airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            Air_Asia = 0

        elif (Airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0
            Air_Asia = 0

        elif (Airline=='Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
            Air_Asia = 0
            
        elif (Airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1
            Air_Asia = 0

        elif (Airline=='Air Asia'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            Air_Asia = 1

        # print(Jet_Airways,
        #     IndiGo,
        #     Air_India,
        #     Multiple_carriers,
        #     SpiceJet,
        #     Vistara,
        #     GoAir,
        #     Multiple_carriers_Premium_economy,
        #     Jet_Airways_Business,
        #     Vistara_Premium_economy,
        #     Trujet)

        # Source
        # Banglore = 0 (not in column)
        #Source = request.form["Source"]
        if (Source == 'Banglore'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Banglore = 1
        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1
            s_Banglore = 0
        elif (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Banglore = 0
          
        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0
            s_Banglore = 0
        
        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0
            s_Banglore = 0
        
        
         
        
            
        #Destination = request.form["Destination"]
        if (Destination == 'Banglore'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Banglore = 1
        elif (Destination == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Banglore = 0
        
        elif (Destination == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Banglore = 0

        elif (Destination == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0
            d_Banglore = 0

        elif (Destination == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1
            d_Banglore = 0
        elif (Destination == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Banglore = 0

        

        prediction=model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_Asia,   ####
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Banglore,   ###
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Banglore, ###
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi,
            
        ]])

        output=round(prediction[0],2)

        return render_template('ff.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("ff.html")

if __name__ == "__main__":
    app.run(debug=True)
#-------------------------------------------------------------------------