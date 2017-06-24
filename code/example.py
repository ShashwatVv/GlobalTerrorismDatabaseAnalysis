import numpy as np
import pandas as pd
import json
import math

pd.options.mode.chained_assignment = None

import plotly.plotly as py
import plotly.graph_objs as go

terror_data = pd.read_csv('datasets/globalterrorismdb_0616dist.csv', encoding='ISO-8859-1', usecols=[0, 1, 2, 3, 8, 11, 13, 14, 29, 35, 84, 100, 103])
terror_data = terror_data.rename(columns={'eventid'         :'id',
                                          'iyear'           :'year',
                                          'imonth'          :'month',
                                          'iday'            :'day',
                                          'country_txt'     :'country',
                                          'provstate'       :'state',
                                          'targtype1_txt'   :'target',
                                          'attacktype1_txt' :'attack',
                                          'weaptype1_txt'   :'weapon',
                                          'nkill'           :'fatalities',
                                          'nwound'          :'injuries'})

data = terror_data[(pd.isnull(terror_data.year)         == False) &
                   (pd.isnull(terror_data.day)          == False) &
                   (pd.isnull(terror_data.country)      == False) &
                   (pd.isnull(terror_data.state)        == False) &
                   (pd.isnull(terror_data.target)       == False) &
                   (pd.isnull(terror_data.attack)       == False) &
                   (pd.isnull(terror_data.weapon)       == False) &
                   (pd.isnull(terror_data.longitude)    == False) &
                   (pd.isnull(terror_data.latitude)     == False) &
                   (pd.isnull(terror_data.fatalities)   == False) &
                   (pd.isnull(terror_data.injuries)     == False) &
                   (terror_data.weapon                  != 'Unknown') &
                   (terror_data.attack                  != 'Unknown') &
                   (terror_data.target                  != 'Unknown') &
                   (terror_data.state                   != 'Unknown') &
                   (terror_data.country                 != 'Unknown')
]

filename = 'terror_filtered_db.csv'
data.to_csv(filename, encoding='utf-8', index=False, index_label=False)
print('Saved ' + str(len(data)) + ' instances to file \'' + filename + '\'')

