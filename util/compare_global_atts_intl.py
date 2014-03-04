import json, pandas


with open('global_attributes.json', 'wb') as fp:
    json.dump(global_attributes, fp)
    
eFile = 'C:\Users\Derrick.Snowden\Documents\GitHub\Real-Time-File-Format\Real-Time-File-Format\WikiFiles\Spray_Seaglider_IMOS_GROOM_Comparison-2013-12-02.xlsx'

xls = pandas.read_excel(eFile, 'GlobalAtts', index_col=None, na_values=['NA'])
tmp = pandas.read_excel(eFile,'acdd',index_col=None,na_values=['NA'])
acdd = tmp.Attribute.copy().dropna()
acdd.name = 'acdd'
acdd.sort()
# ioos = Unnamed: 8, imos = Unnamed: 11, ego = Unnamed: 14
df = pandas.DataFrame(xls[['Unnamed: 8','Unnamed: 11','Unnamed: 14']],columns=['ioos','imos','ego'])
df[['ioos','imos','ego']] = xls[['Unnamed: 8','Unnamed: 11','Unnamed: 14']]
df2=df.iloc[4:].copy()

ioos = df2.ioos.dropna()
ioos.sort()
imos = df2.imos.dropna()
imos.sort()
ego = df2.ego.dropna()
ego.sort()

joint = pandas.concat([acdd,ioos,imos,ego], join='outer', axis = 1)


criterion = df['ioos'].map(lambda x: x.startswith('acknowledgment'))

