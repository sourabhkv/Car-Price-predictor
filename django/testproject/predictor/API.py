import pandas as pd
import joblib
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning)

class MyAPI:
    def __init__(self) -> None:
        
        self.model = joblib.load('randomforest.pkl')
        self.model_encoder = joblib.load('model_encoder.pkl')
        self.make_encoder = joblib.load('make_encoder.pkl')
        self.color_encoder = joblib.load('color_encoder.pkl')
        self.location_encoder = joblib.load('location_encoder.pkl')
        
        self.transmission = {'Manual':0, 'Automatic':1}
        self.fuel_type = {'Petrol':1, 'Diesel':2 ,'CNG':3, 'LPG':4, 'Electric':5, 'CNG + CNG':6, 'Hybrid':7, 'Petrol + CNG':8, 'Petrol + LPG':9}
        self.owner = {'First':1, 'Second':2, 'Third':3, 'Fourth':4, 'UnRegistered Car':0, '4 or More':5}
        self.seller_type = {'Corporate':1, 'Individual':2, 'Commercial Registration':3}
        self.drivetrain = {'FWD':1, 'RWD':2, 'AWD':3}

        self.transmission_list = list(self.transmission.keys())
        self.fuel_type_list = list(self.fuel_type.keys())
        self.owner_list = list(self.owner.keys())
        self.seller_type_list = list(self.seller_type.keys())
        self.drivetrain_list = list(self.drivetrain.keys())

    def predict(self,**kwargs):
        try:
            _maker = self.make_encoder.transform([kwargs.get('car')])[0]
            _model = self.model_encoder.transform([kwargs.get('model')])[0]
            _year = int(kwargs.get('yr')[0])
            _km = int(kwargs.get('km')[0])
            _engine = int(kwargs.get('eng')[0])
            _seat = int(kwargs.get('seat')[0])
            _fuel_tank = int(kwargs.get('fuel-tank_')[0])
            _torque = int(kwargs.get('torque')[0])
            _power = int(kwargs.get('power')[0])
            _transmission = self.transmission[kwargs.get('transmission')[0]]
            _fuel = self.fuel_type[kwargs.get('fuel')[0]]
            _location = self.location_encoder.transform([kwargs.get('location')[0]])[0]
            _color = self.color_encoder.transform([kwargs.get('color')[0]])[0]
            _owner = self.owner[kwargs.get('owner')[0]]
            _seller_type = self.seller_type[kwargs.get('seller')[0]]
            _drivetrain = self.drivetrain[kwargs.get('drive')[0]]
            data = [_maker,_model,_year,_km,_fuel,_transmission,_location,_color,_owner,_seller_type,_engine,_drivetrain,_seat,_fuel_tank,_torque,_power]
            #print(data)
            df = pd.DataFrame([data])
            print(str(self.model.predict(df)[0]))
            return str(self.model.predict(df)[0])
        except:
            return 0