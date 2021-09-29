from lxml import html
import xmltodict
from urllib.parse import urlencode, quote_plus, unquote
import requests
import bs4
import json
import zipfile

a = requests.get('https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key='+API_KEY)
import requests, zipfile
from io import BytesIO
with zipfile.ZipFile(BytesIO(a.content)) as zipfile:
    zipfile.extractall('.')

import pandas as pd
df = pd.read_xml('CORPCODE.xml')
print(df)
