import pandas as pd
import json

def get_data_area(sheetname='Hydro Generation - TWh'):
    df=pd.read_excel('bp-stats-review-2021-all-data.xlsx',sheet_name=sheetname,header=2,index_col=0)
    df_area=df.loc[['Total North America','Total S. & Cent. America','Total Europe',
                    'Total CIS','Total Middle East','Total Africa','Total Asia Pacific']]
    
    # df_area=df_area.iloc[:,:-5]
    return df_area

#得到某一年的数据，默认为2020年
def get_data_year(sheetname='Hydro Generation - TWh',year='2020'):
    df_area=get_data_area(sheetname)
    df_year=df_area[int(year)]
    return df_year

def get_country_data(sheetname='Sheet1'):
    df=pd.read_excel('data/Hydro Generation - TWh.xlsx',sheet_name=sheetname,header=None) #,header=1,index_col=0
    print(df.iloc[0, 0])
    datas = []
    # for data in df.itertuples():
    #     name = data[0]
    #     if(name == 'Total North America' or name == 'Total S. & Cent. America' or name == 'Total Europe' or name == 
    #                 'Total CIS' or name == 'Total Middle East' or name == 'Total Africa' or name == 'Total Asia Pacific'
    #                 or name == 'Total World'):
    #         continue   
    #     initalYear = 1965
    #     for i in range(1, len(data)):
    #         datas.append({'country':name, 'data':data[i], 'year': initalYear})
    #         initalYear += 1
    for j in range(1, df.columns.size):
        for i in range(1, df.shape[0]):
            datas.append({'country':df.iloc[i, 0], 'data':df.iloc[i, j], 'year': df.iloc[0, j]})
    # print(datas)
    res = json.dumps(datas, ensure_ascii=False)
    print(res)
     # 生成对应的JSON数据文件
    content = '{}'.format(res)

    # 写入文件
    with open(r'data/data.json', 'w', encoding="utf-8") as f:
        f.write(content)
    
if  __name__=='__main__':
    df_area=get_data_area()
    # print(df_area.columns[:-2])
    # print(list(df_area.iloc[0,:]))

    all_countries = get_country_data()
    # df_year=get_data_year()
    # print(df_year)