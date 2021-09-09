# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 16:03:19 2021

@author: mohaa
"""

import pandas as pd
import numpy as np
from datetime import date
import xlsxwriter

df = pd.read_csv(r'C:\Users\mohaa\Desktop\Projects and papers\Open entrance\Open Entrance\DR data\The latest data\Full_potential.V3.csv', parse_dates=["subannual"])
df["subannual"] = pd.to_datetime(df["subannual"], format='%m-%d %H:%M+%S:%f')
print (df["subannual"])

### Data aggregation over node "DE" ###
def country(country_name):
    df["region"] = np.where(df["region"].str.startswith(country_name), country_name,df["region"])
    return df.loc[:,('region', 'variable', 'subannual', '2020', '2025', '2030', '2035', '2040', '2045', '2050')]


var = ['Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Dish Washer',
       'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Dryer',
       'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Space Heater',
       'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Space Heater',
       'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Washing Machine',
       'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Water Heater',
       'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Water Heater',
       'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Air Conditioning',
       'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Air Conditioning',
       'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Dish Washer',
       'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Dryer',
       'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Electric Vehicle',
       'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Electric Vehicle',
       'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Refrigeration',
       'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Refrigeration',
       'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Washing Machine']

time = ['2020', '2025', '2030', '2035', '2040', '2045', '2050']

country('DE')

country_names = ['AT', 'BE', 'BG', 'CH', 'CY', 'CZ', 'DE', 'DK', 'EE', 'EL','ES','FI',
                 'FR','HR','HU','IE','IT','LT','LU','LV','NL', 'NO', 'PL', 'PT','RO', 'SE',
                 'SI','SK','TR','UK']

#D = country('DE')[(country('DE')["region"] == "DE") & (country('DE')["variable"] == 'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Dish Washer')]
#c = 'DE'
def Per_country(c):
    group = []
    for item in var:
        if item == 'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Dish Washer':   
            Dis_DW = country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Dis_DW)

        elif item == 'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Dryer':
            Dis_Dr =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Dis_Dr)
            
        elif item == 'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Space Heater':
            Dis_SH =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Dis_SH)
            
        elif item == 'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Space Heater':
            Red_SH =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Red_SH)
            
        elif item == 'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Washing Machine':
            Dis_WM =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Dis_WM)
            
        elif item == 'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Water Heater':
            Dis_WH =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Dis_WH)
            
        elif item == 'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Water Heater':
            Red_WH =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Red_WH)
            
        elif item == 'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Air Conditioning':
            Red_AC =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Red_AC)
            
        elif item == 'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Air Conditioning':
            Dis_AC =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Dis_AC)
            
        elif item == 'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Dish Washer':
            Red_DW =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Red_DW)
            
        elif item == 'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Dryer':
            Red_Dr =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Red_Dr)
            
        elif item == 'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Electric Vehicle':
            Red_EV =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Red_EV)
            
        elif item == 'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Electric Vehicle':
            Dis_EV =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Dis_EV)
            
        elif item == 'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Refrigeration':
            Red_Re =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Red_Re)
            
        elif item == 'Demand Response|Maximum Dispatch|Load Shifting|Electricity|Residential|Refrigeration':
            Dis_Re =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Dis_Re)
            
        elif item == 'Demand Response|Maximum Reduction|Load Shifting|Electricity|Residential|Washing Machine':
            Red_WM =  country(c)[(country(c)["region"] == c) & (country(c)["variable"] == item)]
            group.append(Red_WM)
            
        else:
            pass
                
        
        
                  
    
    
    def tech(name):
        date_value = {}
        for i in name['subannual']:
            if i not in date_value:
                date_value[i] = name[(name['subannual']== i)].loc[:,('2020', '2025', '2030', '2035', '2040', '2045', '2050')].sum(axis=0)
            else:
                pass
            
        return date_value
    
    
    Di_DW = pd.DataFrame.from_dict(tech(Dis_DW), orient='index')
    Di_Dr = pd.DataFrame.from_dict(tech(Dis_Dr), orient='index')
    Di_SH = pd.DataFrame.from_dict(tech(Dis_SH), orient='index')
    Di_WH = pd.DataFrame.from_dict(tech(Dis_WH), orient='index')
    Di_WM = pd.DataFrame.from_dict(tech(Dis_WM), orient='index')
    Di_AC = pd.DataFrame.from_dict(tech(Dis_AC), orient='index')
    Di_EV = pd.DataFrame.from_dict(tech(Dis_EV), orient='index')
    Di_Re = pd.DataFrame.from_dict(tech(Dis_Re), orient='index')
    
    Re_WH = pd.DataFrame.from_dict(tech(Red_WH), orient='index')
    Re_SH = pd.DataFrame.from_dict(tech(Red_SH), orient='index')
    Re_AC = pd.DataFrame.from_dict(tech(Red_AC), orient='index')
    Re_DW = pd.DataFrame.from_dict(tech(Red_DW), orient='index')
    Re_Dr = pd.DataFrame.from_dict(tech(Red_Dr), orient='index')
    Re_EV = pd.DataFrame.from_dict(tech(Red_EV), orient='index')
    Re_Re = pd.DataFrame.from_dict(tech(Red_Re), orient='index')
    Re_WM = pd.DataFrame.from_dict(tech(Red_WM), orient='index')
    
    dfs = {'Dispatch_DishWasher': Di_DW, 'Dispatch_Dryer' : Di_Dr, 'Dispatch_SpaceHeater' : Di_SH, 'Reduction_SpaceHeater' : Re_SH, 'Dispatch_WashingMachine': Di_WM,
           'Dispatch_WaterHeater': Di_WH, 'Reduction_WaterHeater': Re_WH, 'Reduction_AirConditioning': Re_AC, 'Dispatch_AirConditioning': Di_AC, 'Reduction_DishWasher': Re_DW, 'Reduction_Dryer': Re_Dr,
           'Reduction_ElectricVehicle': Re_EV, 'Dispatch_ElectricVehicle': Di_EV, 'Reduction_Refrigeration': Re_Re, 'Dispatch_Refrigeration': Di_Re, 'Reduction_WashingMachine': Re_WM}
    
    
    writer = pd.ExcelWriter(r'C:\Users\mohaa\Desktop\Projects and papers\Open entrance\Open Entrance\DR data\The latest data\countries data' +"/"+ str(c) + '.xlsx', engine= 'xlsxwriter')
    
    for sheet_name in dfs.keys():
        dfs[sheet_name].to_excel(writer, sheet_name=sheet_name)
            
    writer.save()


for c in country_names:
    Per_country(c)
    
    
    




