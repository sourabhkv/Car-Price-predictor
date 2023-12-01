from django.shortcuts import render
import pandas as pd
from .API import MyAPI

data = pd.read_csv("Car_datal.csv")
unique_car = list(data['Make'].unique())
unique_car.sort()

location_list = list(data['Location'].unique())
location_list.sort()

color_list = list(data['Color'].unique())
color_list.sort()

fuel_type = list(data['Fuel Type'].unique())
fuel_type.sort()

transmission_type = ['Manual','Automatic']
owner_type = ['First','Second','Third','Fourth','UnRegistered Car','4 or More']
seller_type = ['Corporate','Individual','Commercial Registration']
drivetrain_type = ['FWD','RWD','AWD']

def car_list(request):
    selected_car = request.POST.get('car')
    selected_model = request.POST.get('model')
    dynamic_label_text = 0
    models = []
    if request.method=='POST':
        x = MyAPI()
        dynamic_label_text = x.predict(**request.POST)
    if selected_car:
        models = list(data[data['Make'] == selected_car]['Model'].unique())
        models.sort()
    return render(request, 'index.html', {'cars': unique_car, 'selected_car': request.POST.get('car'), 'models': models, 
                                          'selected_model': selected_model, 'fuel_type': fuel_type, 'transmission_type': transmission_type,
                                            'color_type': color_list, 'location_type': location_list, 'owner_type': owner_type,
                                            'seller_type': seller_type,'drive_type':drivetrain_type,'selected_year': request.POST.get('yr'),
                                            'selected_capacity': request.POST.get('seat'), 'selected_fuel_tank': request.POST.get('fuel-tank_'),
                                            'selected_torque': request.POST.get('torque'), 'selected_power': request.POST.get('power'),
                                            'selected_kilometer': request.POST.get('km'), 'selected_eng': request.POST.get('eng'),
                                            'dynamic_label_text': dynamic_label_text, 'selected_color' : request.POST.get('color'),
                                            'selected_fuel': request.POST.get('fuel'), 'selected_transmission': request.POST.get('transmission'),
                                            'selected_location': request.POST.get('location'), 'selected_owner': request.POST.get('owner'),
                                            'selected_seller': request.POST.get('seller'), 'selected_drive': request.POST.get('drive'),
                                            })