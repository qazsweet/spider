from urllib import request
import json
import pandas as pd

herb = 'Citrus%20Reticulata' #licorice

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
url= 'http://tcmspw.com/tcmspsearch.php?qr='+str(herb)+'&qsr=herb_en_name&token=9282669d641bcfa010b2c5447daf5a68'
params = {"data-page":2}
req = request.Request(url=url, headers=headers)
with request.urlopen(req) as response:
    data1 = response.read().decode('utf-8') 

def saveFile(data):
    save_path = r'C:\Users\TianMG\Desktop/req2.txt'
    f_obj = open(save_path, 'w', encoding="utf-8") # w 表示打开方式,也可用wb
    f_obj.write(data)
    f_obj.close()
 
saveFile(data1)

dataset = data1.split('<script>')
target = dataset[6].split('#grid')

def saveExcel(rowinfo, excelName):
    rowinfo[-1]=rowinfo[-1].split('}')[0]
    data = []
    for i in range(len(rowinfo)):
        j = json.loads('[{'+rowinfo[i]+'}]')
        data.append(j)
    df = pd.DataFrame()
    for line in data:
        for i in line:
            df1 = pd.DataFrame([i])
            df = df.append(df1)
    df.to_excel(excelName, sheet_name='Data', startcol=0, index=False)
        

# first grid
rowinfo = target[1][67:].split('},{')
saveExcel(rowinfo, str(herb)+'_data1.xlsx')

# second grid
rowinfo = target[2][68:].split('},{')
saveExcel(rowinfo, str(herb)+'_data2.xlsx')

rowinfo = target[3][69:].split('},{')
saveExcel(rowinfo, str(herb)+'_data3.xlsx')

rowinfo = target[4][68:].split('},{')
saveExcel(rowinfo, str(herb)+'_data4.xlsx')

rowinfo = target[5][69:].split('},{')
saveExcel(rowinfo, str(herb)+'_data5.xlsx')
