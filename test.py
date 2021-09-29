# Cybos 실행
# import pywinauto
# app = pywinauto.application.Application()
# app.start("C:\\Users\\hongs\\Desktop\\project\\Project\\Trade\\Cybos\\STARTER\\ncStarter.exe")

#
import pandas as pd
df = pd.read_xml('CORPCODE.xml')
df = df.fillna('')
df= df[df['stock_code'] != '']
print(df)