import pandas as pd

# first xlsx file upload to colab and then to the notebook
SPC_Daten = pd.read_excel('/content/SPC_Daten.xlsx') 

# index names
index = ['a','b','c','d','e','f','g']
SPC_Daten.index = index

# drop the nan values
SPC_Daten = SPC_Daten.drop('a',axis=0)

# new index
SPC_Daten =  SPC_Daten.set_index(SPC_Daten.columns[0])

# transform the data Frame
SPC_Daten_T = SPC_Daten.T

# new index and renaming columns
index = range(len(SPC_Daten_T))
SPC_Daten_T.index = index
SPC_Daten_T = SPC_Daten_T.rename(columns={
    '1. Signal Rausch Verhältnis':'index',
    'CFD Schwellenspannung in mV':'cfd_ss [mV]',
    'Maximum A':'Max',
    'Halbwertsbreite in ns':'HWB [ns]',
    'Mittleres Rauschen R':'MR',
    'SNR = A/R':'SNR = Max/MR',
    'total count':'tc'
    })

# float numbers into integers, if there look like integers
for i in range(len(SPC_Daten_T)):
  SPC_Daten_T.at[i,'cfd_ss [mV]'] = int(SPC_Daten_T.at[i,'cfd_ss [mV]'])
  SPC_Daten_T.at[i,'Max'] = int(SPC_Daten_T.at[i,'Max'])
  SPC_Daten_T.at[i,'tc'] = int(SPC_Daten_T.at[i,'tc'])

# data frame into csv file
SPC_Daten_T.to_csv('SPCD.csv',index=True,sep=',')
