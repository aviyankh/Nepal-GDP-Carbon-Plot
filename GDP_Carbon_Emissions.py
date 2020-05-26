import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gdpw = pd.read_csv('D:/GDP.csv' , skiprows = 3)
cobw = pd.read_csv('D:/COX_emission.csv' , skiprows=3)

gdpw.set_index('Country Name' ,inplace=True)
cobw.set_index('Country Name' , inplace = True)

np_gdp = gdpw.loc['Nepal']
np_co = cobw.loc['Nepal']

np_gdp = np_gdp.T
np_co = np_co.T

np_gdp = np_gdp.drop(['Country Code','Indicator Name'  , 'Indicator Code' , '2019' , '2018' , '2017', '2016', '2015'])
np_co = np_co.drop(['Country Code','Indicator Name'  , 'Indicator Code' , '2019' , '2018' , '2017', '2016', '2015'])

np_gdp = np_gdp.T
np_co = np_co.T

nipx = list(np_gdp.index)


np_gdp.columns = ['Year' , 'GDP(in billions)']
np_co.columns = ['Year' , 'Emissions']

gdplist = list(pd.to_numeric(np_gdp[0:])/1000000000)
colist = list(pd.to_numeric(np_co[0:])/1000)
del gdplist[-1] , nipx[-1] , colist[-1]


fig, ax1 = plt.subplots()
ax1.plot(gdplist , color = 'red' , linewidth = 3 , label = 'GDP per Year')

ax1.yaxis.label.set_color('red')
ax1.set_xlabel('Years')
ax1.set_ylabel('GDP in Billions')


ax2 = ax1.twinx()
ax2.plot(nipx , colist , color = 'blue' , linewidth = 3 , label  = 'Carbon Emissons per Year')
ax2.set_ylabel('Carbon Emissions in kilotons')
ax2.yaxis.label.set_color('blue')
plt.xticks([nipx[0] , nipx[11] , nipx[22] , nipx[33] ,nipx[44], nipx[-1]] , visible=True, rotation="horizontal")

ax1.legend(loc='upper left')
ax2.legend(loc='lower right')

plt.title('GDP vs Carbon Emission of Nepal From 1960-2014')
fig.tight_layout()
plt.show()

