from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import sys
import pandas as pd
import joblib


class MyGUI(QMainWindow):
    def __init__(self,*args):
        self.__version__ = 1.01
        super(MyGUI, self).__init__()
        uic.loadUi('project.ui', self)
        self.setWindowIcon(QIcon('car.ico'))

        self.model = joblib.load('randomforest.pkl')
        self.model_encoder = joblib.load('model_encoder.pkl')
        self.make_encoder = joblib.load('make_encoder.pkl')
        self.color_encoder = joblib.load('color_encoder.pkl')
        self.location_encoder = joblib.load('location_encoder.pkl')

        self.cars_data = pd.read_csv("Car details v4.csv")
        self.cars_makers = self.cars_data['Make'].unique()
        self.cars_makers.sort()
        self.cars_colors = self.cars_data['Color'].unique()
        self.cars_colors.sort()
        self.cars_location = self.cars_data['Location'].unique()
        self.cars_location.sort()
        self.cars_models = self.cars_data.loc[self.cars_data['Make']=='Audi','Model'].unique()
        self.cars_models.sort()
        

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

        self.comboBox_2.addItems(self.cars_models)
        self.comboBox_3.addItems(self.transmission_list)
        self.comboBox_4.addItems(self.fuel_type_list)
        self.comboBox_7.addItems(self.owner_list)
        self.comboBox_8.addItems(self.seller_type_list)
        self.comboBox_9.addItems(self.drivetrain_list)
        self.comboBox_5.addItems(self.cars_location)
        self.comboBox_6.addItems(self.cars_colors)
        self.comboBox.addItems(self.cars_makers)
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
        self.label_18.setText('')

        self.pushButton.clicked.connect(self.predict)
        self.pushButton_2.clicked.connect(self.clear)

        self.show()
    
    def on_combobox_changed(self):
        self.comboBox_2.clear()
        self.cars_models = self.cars_data.loc[self.cars_data['Make']==self.comboBox.currentText(),'Model'].unique()
        self.cars_models.sort()
        self.comboBox_2.addItems(self.cars_models)
    
    def predict(self):
        try:
            _maker = self.make_encoder.transform([self.comboBox.currentText()])[0]
            _model = self.model_encoder.transform([self.comboBox_2.currentText()])[0]
            _year = int(self.plainTextEdit.toPlainText())
            _km = int(self.plainTextEdit_2.toPlainText())
            _engine = int(self.plainTextEdit_4.toPlainText())
            _seat = int(self.plainTextEdit_3.toPlainText())
            _fuel_tank = int(self.plainTextEdit_5.toPlainText())
            _torque = int(self.plainTextEdit_6.toPlainText())
            _power = int(self.plainTextEdit_7.toPlainText())
            _transmission = self.transmission[self.comboBox_3.currentText()]
            _fuel = self.fuel_type[self.comboBox_4.currentText()]
            _location = self.location_encoder.transform([self.comboBox_5.currentText()])[0]
            _color = self.color_encoder.transform([self.comboBox_6.currentText()])[0]
            _owner = self.owner[self.comboBox_7.currentText()]
            _seller_type = self.seller_type[self.comboBox_8.currentText()]
            _drivetrain = self.drivetrain[self.comboBox_9.currentText()]
            data = [_maker,_model,_year,_km,_fuel,_transmission,_location,_color,_owner,_seller_type,_engine,_drivetrain,_seat,_fuel_tank,_torque,_power]
            df = pd.DataFrame([data])
            _res = str(self.model.predict(df)[0])
            self.label_18.setText('₹ '+_res)
        except:
            self.label_18.setText('Enter all details')
    
    def clear(self):
        self.plainTextEdit.setPlainText('')
        self.plainTextEdit_2.setPlainText('')
        self.plainTextEdit_3.setPlainText('')
        self.plainTextEdit_4.setPlainText('')
        self.plainTextEdit_5.setPlainText('')
        self.plainTextEdit_6.setPlainText('')
        self.plainTextEdit_7.setPlainText('')
        self.label_18.setText('')

def main():
    app = QApplication([])
    window = MyGUI(*sys.argv)
    app.exec_()

if __name__ == '__main__':
    main()