import pandas as pd
import re

double_list = [[1000, '과자','2019-12-31','반품'],
 [2000, '음료', '2020-03-02', '정상'],
 [3000, '아이스크림', '2020-02-03','정상'],
 [1000,'과자','2019-12-31','반품']]
pd.DataFrame(data = double_list)

double_columns = ['가격','종류','판매일자','반품여부']
df_saledays = pd.DataFrame(data=double_list, columns=double_columns)
# print(df_saledays)

# regexpress(정규식)
data = {"Names" : ["김지수", "박지민", "이태용", "최수영"]}
df_Name = pd.DataFrame(data)
print(df_Name)

pattern = r"^([(가-힣)])"
df_Name_extract = df_Name["Names"].str.extract(pattern)
print(df_Name_extract)
