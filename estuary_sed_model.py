# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:28:44 2024

@author: murph
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#define the annual sediment volume in m^3
sed_vol = 10**6

#define the total area of the estuary in m
total_area = 1.5*10**8

#restrict area to open water
#define the open water area as owa of the estuary in m^2
#this will be used in both elevation and sea level calculations
owa = total_area*0.6

#define the starting sea level
slh = 1.6

#Next we define the open water volume as omv in m^3
#Expressed as 1.6 m depth x owa

omv = owa*slh

#now we have an expression of voolume, but this may be discarded as 
#I believe that we can simplify to a 1-Dimensional model.

#define subsidence rate subs
subs = 0.003

#define sea level rise slr
slr = 0.002
#set starting elevation at 0
ele = 0

#define temporal range of model
years = range(1,52)
year = 0
#set up a dataframe for elevation of sediment and sea level
Estuary_basic = {'Sea Level': [1.6, slh],
                        'Elevation': [0, ele],
                        'Year' : [0, 1],
                        }
Estuary_basic_df = pd.DataFrame(Estuary_basic)
Estuary_SLR1 = Estuary_basic_df
Estuary_SLR2 = Estuary_basic_df
Estuary_SLR3 = Estuary_basic_df
Estuary_SLRfun = Estuary_basic_df

# 80% volume remaining after 20% consolidation, times the sediment volume, divided by the open water area 
ele_change = 0.8*sed_vol/owa
    
## Basic Model
for elevation in years:
        if year >= 50:
            print('local sea level has not been overcome by sedimentary processes by the end of model runs.')
            print(Estuary_basic_df)
            break
        elif ele > slh:
            print("Elevation overcomes sea level at year: ", year)
            print(Estuary_basic_df)
            break
        else:
            year += 1
            print("At year: ", year)
            # accretion minus subsidence
            ele += ele_change - subs
            print('elevation = ' , ele, 'meters')
            #increase sea level by sea level rise (unchanging)
            slh += slr
            df = pd.DataFrame({'Sea Level':[slh],
                               'Elevation':[ele],
                               'Year':[year]})
            Estuary_basic_df = pd.concat([Estuary_basic_df, df], axis= 0)
            print("sea level = ", slh, "meters")

Estuary_basic_df['Depth'] = Estuary_basic_df['Sea Level'] - Estuary_basic_df['Elevation']


#reset values        
ele = 0
year = 0
slh = 1.6
slr = 0.002
#Scenario with 0.02 SLR acceleration
for elevation in years:
        if year >= 50:
            print('local sea level has not been overcome by sedimentary processes by the end of model runs.')
            print(Estuary_SLR1)
            break
        elif ele > slh:
            print("Elevation overcomes sea level at year: ", year)
            print(Estuary_SLR1)
            break
        else:
            year += 1
            print("At year: ", year)
            # accretion minus subsidence
            ele += ele_change - subs
            print('elevation = ' , ele, 'meters')
            #increase sea level by sea level rise 
            slr += slr*0.02
            slh += slr
            df = pd.DataFrame({'Sea Level':[slh],
                               'Elevation':[ele],
                               'Year':[year]})
            Estuary_SLR1 = pd.concat([Estuary_SLR1, df], axis= 0)
            print("sea level = ", slh, "meters")

Estuary_SLR1['Depth'] = Estuary_SLR1['Sea Level'] - Estuary_SLR1['Elevation']


#reset values
ele= 0
year = 0
slh = 1.6
slr = 0.002
#Scenario with 0.05 SLR acceleration
for elevation in years:
        if year >= 50:
            print('local sea level has not been overcome by sedimentary processes by the end of model runs.')
            print(Estuary_SLR2)
            break
        elif ele > slh:
            print("Elevation overcomes sea level at year: ", year)
            print(Estuary_SLR2)
            break
        else:
            year += 1
            print("At year: ", year)
            # accretion minus subsidence
            ele += ele_change - subs
            print('elevation = ' , ele, 'meters')
            #increase sea level by sea level rise 
            slr += slr*0.05
            slh += slr
            df = pd.DataFrame({'Sea Level':[slh],
                               'Elevation':[ele],
                               'Year':[year]})
            Estuary_SLR2 = pd.concat([Estuary_SLR2, df], axis= 0)
            print("sea level = ", slh, "meters")
Estuary_SLR2['Depth'] = Estuary_SLR2['Sea Level'] - Estuary_SLR2['Elevation']

#reset values
ele = 0
year = 0
slh = 1.6
slr = 0.002

#Scenario with 0.07 SLR acceleration
for elevation in years:
        if year >= 50:
            print('local sea level has not been overcome by sedimentary processes by the end of model runs.')
            print(Estuary_SLR3)
            break
        elif ele > slh:
            print("Elevation overcomes sea level at year: ", year)
            print(Estuary_SLR3)
            break
        else:
            year += 1
            print("At year: ", year)
            # accretion minus subsidence
            ele += ele_change - subs
            print('elevation = ' , ele, 'meters')
            #increase sea level by sea level rise 
            slr += slr*0.07
            slh += slr
            df = pd.DataFrame({'Sea Level':[slh],
                               'Elevation':[ele],
                               'Year':[year]})
            Estuary_SLR3 = pd.concat([Estuary_SLR3, df], axis= 0)
            print("sea level = ", slh, "meters")

Estuary_SLR3['Depth'] = Estuary_SLR3['Sea Level'] - Estuary_SLR3['Elevation']

Scenario_1_plot = Estuary_basic_df.plot.line(x='Year', title = 'Scenario 1: No Acceleration to SLR', ylabel = 'meters')
Scenario_2_plot = Estuary_SLR1.plot.line(x='Year', title = 'Scenario 2: 2% Acceleration in SLR', ylabel = 'meters')
Scenario_3_plot = Estuary_SLR2.plot.line(x='Year', title = 'Scenario 3: 5% Acceleration in SLR', ylabel = 'meters')
Scenario_4_plot = Estuary_SLR3.plot.line(x='Year', title = 'Scenario 4: 7% Acceleration in SLR', ylabel = 'meters')


#For Fun ! Make elevation overtake SLR 
ele = 0
year = 0
slh = 1.6
slr = 0.002
ele_change_fun = 0.08
#Scenario with 0.07 SLR acceleration
for elevation in years:
        if year >= 50:
            print('local sea level has not been overcome by sedimentary processes by the end of model runs.')
            print(Estuary_SLRfun)
            break
        elif ele > slh:
            print("Elevation overcomes sea level at year: ", year)
            print(Estuary_SLRfun)
            break
        else:
            year += 1
            print("At year: ", year)
            # accretion minus subsidence
            ele += ele_change_fun - subs
            print('elevation = ' , ele, 'meters')
            #increase sea level by sea level rise 
            slr += slr*0.07
            slh += slr
            df = pd.DataFrame({'Sea Level':[slh],
                               'Elevation':[ele],
                               'Year':[year]})
            Estuary_SLRfun = pd.concat([Estuary_SLRfun, df], axis= 0)
            print("sea level = ", slh, "meters")

Estuary_SLRfun['Depth'] = Estuary_SLRfun['Sea Level'] - Estuary_SLRfun['Elevation']


Scenario_fun_plot = Estuary_SLRfun.plot.line(x='Year', title = 'Scenario fun: Vertical Accretion = 8 cm / year and a 7% Acceleration in SLR', ylabel = 'meters')
