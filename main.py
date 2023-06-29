import pandas as pd

car=pd.read_csv('quikr_car.csv')

#print(car.head())
#print(car.shape)

#print(car['year'].unique())

#print(car['Price'].unique())

#print(car['kms_driven'].unique())

#print(car['fuel_type'].unique())

backup=car.copy()
#print(backup)

#print(car[car['year'].str.isnumeric()])
car=car[car['year'].str.isnumeric()]

car['year']=car['year'].astype(int)

#print(car['year'])

#print(car.info())

#print(car[car['Price']!='Ask for Price'])

car=car[car['Price'] !="Ask For Price"]

#print(car['Price'])

car['Price']=car['Price'].str.replace(',','').astype(int)

#print(car['Price'])

#print(car.info())

#print(car['kms_driven'])

car['kms_driven']=car['kms_driven'].str.split(' ').str.get(0).str.replace(',','')


car=car[car['kms_driven'].str.isnumeric()]

car['kms_driven']=car['kms_driven'].astype(int)

#print(car['kms_driven'])

#print(car.info())

#print(car[~car['fuel_type'].isna()])

car=car[~car['fuel_type'].isna()]

car['name']=car['name'].str.split().str.slice(0,3).str.join(' ')

car=car.reset_index(drop=True)

#print(car)

#print(car.describe())
car=car[car['Price']<6e6].reset_index(drop=True)
#print(car.describe())
car.to_csv('cleaned.csv')