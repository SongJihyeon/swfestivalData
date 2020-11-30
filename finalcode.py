#import(알아서 하면 됨)
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
#지도그리기 위한 import
from pandas import Series, DataFrame
import numpy as np
import matplotlib
import folium
from folium.plugins import HeatMap, MarkerCluster, TimestampedGeoJson
from folium.features import DivIcon
import warnings
import json

#경고메시지 없애기
warnings.simplefilter(action = "ignore",category=FutureWarning)

#구글 드라이브에서 파일 불러오기
from google.colab import drive
drive.mount('/content/drive/')

matplotlib.rcParams['font.family'].insert(0, 'Malgun Gothic')
%matplotlib inline

#변수명 = csv 경로랑 파일 읽어오는 코드
card = pd.read_csv('/content/drive/My Drive/sw 페스티벌 코로나 데이터/card_20200717.csv')
#SeoulFloating.csv 데이터 확인
seoulfloat = pd.read_csv('drive/My Drive/2020대회공식데이터패키지/COVID19_확진자데이터/SeoulFloating.csv')

#json 파일 불러오기
geo_path = 'drive/My Drive/sw 페스티벌 코로나 데이터/skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path,encoding='utf-8'))

#서울시 유동인구 데이터 다듬기
float_ = seoulfloat.rename({'date':'일자','hour' : '시간단위','birth_year' : '연령대', 'sex':'성별', 'province' : '지역','city':'구','fp_num' : '유동인구'},axis='columns')

from datetime import datetime
date = []

for data in float_['일자'] :
    date.append(datetime.strptime(str(data), '%Y-%m-%d'))
float_['일자'] = date
float_

float_gu = float_.pivot_table(index = '일자', columns = '구', values = '유동인구', aggfunc = 'sum')  # time == 24 // non-time 
float_gu.rename( columns = {'Dobong-gu' : '도봉구', 'Dongdaemun-gu' : '동대문구', 'Dongjag-gu' : '동작구', 'Eunpyeong-gu' : '은평구', 'Gangbuk-gu' : '강북구', 'Gangdong-gu' : '강동구', 'Gangnam-gu' : '강남구', 'Gangseo-gu' : '강서구', 'Geumcheon-gu' : '금천구', 'Guro-gu': '구로구', 'Gwanak-gu' : '관악구', 'Gwangjin-gu' : '광진구', 'Jongno-gu' : '종로구', 'Jung-gu' :'중구', 'Jungnang-gu' : '중랑구', 'Mapo-gu' : '마포구', 'Nowon-gu' : '노원구', 'Seocho-gu' : '서초구', 'Seodaemun-gu':'서대문구', 'Seongbuk-gu':'성북구','Seongdong-gu':'성동구','Songpa-gu':'송파구', 'Yangcheon-gu':'양천구', 'Yeongdeungpo-gu':'영등포구','Yongsan-gu':'용산구'},inplace=True)
float_gu

#동 코드, 동, 업종만 뽑아내기
region_induty = ['adstrd_code','receipt_dttm', 'salamt']
card_select = card[region_induty]
card_select

#강동구
kangdonggu_select = card_select[(card_select['adstrd_code']>=1174000000) & (card_select['adstrd_code']<=1175000000)]
kangdonggu_select = kangdonggu_select[['receipt_dttm', 'salamt']]
#금천구
gemcheongu_select = card_select[(card_select['adstrd_code']>=1154500000) & (card_select['adstrd_code']<=1154600000)]
gemcheongu_select = gemcheongu_select[['receipt_dttm', 'salamt']]
#구로구
gurogu_select = card_select[(card_select['adstrd_code']>=1153000000) & (card_select['adstrd_code']<=1153100000)]
gurogu_select = gurogu_select[['receipt_dttm', 'salamt']]
#강서구
gangseogu_select = card_select[(card_select['adstrd_code']>=1150000000) & (card_select['adstrd_code']<=1151000000)]
gangseogu_select = gangseogu_select[['receipt_dttm', 'salamt']]
#양천구
yangcheongu_select = card_select[(card_select['adstrd_code']>=1147000000) & (card_select['adstrd_code']<=1148000000)]
yangcheongu_select = yangcheongu_select[['receipt_dttm', 'salamt']]
#마포구
mapogu_select = card_select[(card_select['adstrd_code']>=1144000000) & (card_select['adstrd_code']<=1145000000)]
mapogu_select = mapogu_select[['receipt_dttm', 'salamt']]
#서대문구
seodaemungu_select = card_select[(card_select['adstrd_code']>=1141000000) & (card_select['adstrd_code']<=1142000000)]
seodaemungu_select = seodaemungu_select[['receipt_dttm', 'salamt']]
#은평구
eunpyeonggu_select = card_select[(card_select['adstrd_code']>=1138000000) & (card_select['adstrd_code']<=1139000000)]
eunpyeonggu_select = eunpyeonggu_select[['receipt_dttm', 'salamt']]
#노원구
nowongu_select = card_select[(card_select['adstrd_code']>=1135000000) & (card_select['adstrd_code']<=1136000000)]
nowongu_select = nowongu_select[['receipt_dttm', 'salamt']]
#도봉구
dobonggu_select = card_select[(card_select['adstrd_code']>=1132000000) & (card_select['adstrd_code']<=1133000000)]
dobonggu_select = dobonggu_select[['receipt_dttm', 'salamt']]
#송파구
songpagu_select = card_select[(card_select['adstrd_code']>=1171000000) & (card_select['adstrd_code']<=1172000000)]
songpagu_select = songpagu_select[['receipt_dttm', 'salamt']]
#강남구
gangnamgu_select = card_select[(card_select['adstrd_code']>=1168000000) & (card_select['adstrd_code']<=1169000000)]
gangnamgu_select = gangnamgu_select[['receipt_dttm', 'salamt']]
#서초구
seochogu_select = card_select[(card_select['adstrd_code']>=1165000000) & (card_select['adstrd_code']<=1166000000)]
seochogu_select = seochogu_select[['receipt_dttm', 'salamt']]
#관악구
gwanakgu_select = card_select[(card_select['adstrd_code']>=1162000000) & (card_select['adstrd_code']<=1163000000)]
gwanakgu_select = gwanakgu_select[['receipt_dttm', 'salamt']]
#동작구
dongjakgu_select = card_select[(card_select['adstrd_code']>=1159000000) & (card_select['adstrd_code']<=1160000000)]
dongjakgu_select = dongjakgu_select[['receipt_dttm', 'salamt']]
#영등포구
yeongdeungpogu_select = card_select[(card_select['adstrd_code']>=1156000000) & (card_select['adstrd_code']<=1157000000)]
yeongdeungpogu_select = yeongdeungpogu_select[['receipt_dttm', 'salamt']]
#강북구
kangbukgu_select = card_select[(card_select['adstrd_code']>=1130500000) & (card_select['adstrd_code']<=1130600000)]
kangbukgu_select = kangbukgu_select[['receipt_dttm', 'salamt']]
#성북구
sungbukgu_select = card_select[(card_select['adstrd_code']>=1129000000) & (card_select['adstrd_code']<=1129100000)]
sungbukgu_select = sungbukgu_select[['receipt_dttm', 'salamt']]
#중랑구
jungranggu_select = card_select[(card_select['adstrd_code']>=1126000000) & (card_select['adstrd_code']<=1126100000)]
jungranggu_select = jungranggu_select[['receipt_dttm', 'salamt']]
#동대문구
dongdaemungu_select = card_select[(card_select['adstrd_code']>=1123000000) & (card_select['adstrd_code']<=1123100000)]
dongdaemungu_select = dongdaemungu_select[['receipt_dttm', 'salamt']]
#광진구
gwangjingu_select = card_select[(card_select['adstrd_code']>=1121500000) & (card_select['adstrd_code']<=1121600000)]
gwangjingu_select = gwangjingu_select[['receipt_dttm', 'salamt']]
#성동구
sungdonggu_select = card_select[(card_select['adstrd_code']>=1120000000) & (card_select['adstrd_code']<=1120100000)]
sungdonggu_select = sungdonggu_select[['receipt_dttm', 'salamt']]
#용산구
yongsangu_select = card_select[(card_select['adstrd_code']>=1117000000) & (card_select['adstrd_code']<=1117100000)]
yongsangu_select = yongsangu_select[['receipt_dttm', 'salamt']]
#중구
junggu_select = card_select[(card_select['adstrd_code']>=1114000000) & (card_select['adstrd_code']<=1114100000)]
junggu_select = junggu_select[['receipt_dttm', 'salamt']]
#종로구
jongrogu_select = card_select[(card_select['adstrd_code']>=1111000000) & (card_select['adstrd_code']<=1111100000)]
jongrogu_select = jongrogu_select[['receipt_dttm', 'salamt']]

#강동구 
kangdonggu = {
    'receipt_dttm': kangdonggu_select['receipt_dttm'],
    'salamt': kangdonggu_select['salamt'],
    '구': "강동구"
}
kangdonggu = DataFrame(kangdonggu)

kangdonggu = kangdonggu.rename( columns = {'receipt_dttm' : '일자'} )

kangdonggu_select_table = kangdonggu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
kangdonggu_select_table

##금천구

gemcheongu = {
    'receipt_dttm': gemcheongu_select['receipt_dttm'],
    'salamt': gemcheongu_select['salamt'],
    '구': "금천구"
}
gemcheongu = DataFrame(gemcheongu)

gemcheongu = gemcheongu.rename( columns = {'receipt_dttm' : '일자'} )

gemcheongu_select_table = gemcheongu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
gemcheongu_select_table

#구로구
gurogu = {
    'receipt_dttm': gurogu_select['receipt_dttm'],
    'salamt': gurogu_select['salamt'],
    '구': "구로구"
}
gurogu = DataFrame(gurogu)

gurogu = gurogu.rename( columns = {'receipt_dttm' : '일자'} )

gurogu_select_table = gurogu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
gurogu_select_table

#강서구
gangseogu = {
    'receipt_dttm': gangseogu_select['receipt_dttm'],
    'salamt': gangseogu_select['salamt'],
    '구': "강서구"
}
gangseogu = DataFrame(gangseogu)

gangseogu = gangseogu.rename( columns = {'receipt_dttm' : '일자'} )

gangseogu_select_table = gangseogu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
gangseogu_select_table

#양천구
yangcheongu = {
    'receipt_dttm': yangcheongu_select['receipt_dttm'],
    'salamt': yangcheongu_select['salamt'],
    '구': "양천구"
}
yangcheongu = DataFrame(yangcheongu)

yangcheongu = yangcheongu.rename( columns = {'receipt_dttm' : '일자'} )

yangcheongu_select_table= yangcheongu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
yangcheongu_select_table

#마포구
mapogu = {
    'receipt_dttm': mapogu_select['receipt_dttm'],
    'salamt': mapogu_select['salamt'],
    '구': "마포구"
}
mapogu = DataFrame(mapogu)

mapogu = mapogu.rename( columns = {'receipt_dttm' : '일자'} )
mapogu_select_table = mapogu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
mapogu_select_table

#서대문구
seodaemungu = {
    'receipt_dttm': seodaemungu_select['receipt_dttm'],
    'salamt': seodaemungu_select['salamt'],
    '구': "서대문구"
}
seodaemungu = DataFrame(seodaemungu)

seodaemungu = seodaemungu.rename( columns = {'receipt_dttm' : '일자'} )
seodaemungu_select_table = seodaemungu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
seodaemungu_select_table

#은평구
eunpyeonggu = {
    'receipt_dttm': eunpyeonggu_select['receipt_dttm'],
    'salamt': eunpyeonggu_select['salamt'],
    '구': "은평구"
}
eunpyeonggu = DataFrame(eunpyeonggu)

eunpyeonggu = eunpyeonggu.rename( columns = {'receipt_dttm' : '일자'} )
eunpyeonggu_select_table = eunpyeonggu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
eunpyeonggu_select_table

#노원구
nowongu = {
    'receipt_dttm': nowongu_select['receipt_dttm'],
    'salamt': nowongu_select['salamt'],
    '구': "노원구"
}
nowongu = DataFrame(nowongu)

nowongu = nowongu.rename( columns = {'receipt_dttm' : '일자'} )
nowongu_select_table = nowongu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
nowongu_select_table

#도봉구
dobonggu = {
    'receipt_dttm': dobonggu_select['receipt_dttm'],
    'salamt': dobonggu_select['salamt'],
    '구': "도봉구"
}
dobonggu = DataFrame(dobonggu)

dobonggu = dobonggu.rename( columns = {'receipt_dttm' : '일자'} )
dobonggu_select_table = dobonggu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
dobonggu_select_table

#송파구
songpagu = {
    'receipt_dttm': songpagu_select['receipt_dttm'],
    'salamt': songpagu_select['salamt'],
    '구': "송파구"
}
songpagu = DataFrame(songpagu)

songpagu = songpagu.rename( columns = {'receipt_dttm' : '일자'} )
songpagu_select_table = songpagu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
songpagu_select_table

#강남구
gangnamgu = {
    'receipt_dttm': gangnamgu_select['receipt_dttm'],
    'salamt': gangnamgu_select['salamt'],
    '구': "강남구"
}
gangnamgu = DataFrame(gangnamgu)

gangnamgu = gangnamgu.rename( columns = {'receipt_dttm' : '일자'} )
gangnamgu_select_table = gangnamgu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
gangnamgu_select_table

#서초구
seochogu = {
    'receipt_dttm': seochogu_select['receipt_dttm'],
    'salamt': seochogu_select['salamt'],
    '구': "서초구"
}
seochogu = DataFrame(seochogu)

seochogu = seochogu.rename( columns = {'receipt_dttm' : '일자'} )
seochogu_select_table = seochogu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
seochogu_select_table

#관악구
gwanakgu = {
    'receipt_dttm': gwanakgu_select['receipt_dttm'],
    'salamt': gwanakgu_select['salamt'],
    '구': "관악구"
}
gwanakgu = DataFrame(gwanakgu)

gwanakgu = gwanakgu.rename( columns = {'receipt_dttm' : '일자'} )
gwanakgu_select_table = gwanakgu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
gwanakgu_select_table

#동작구
dongjakgu = {
    'receipt_dttm': dongjakgu_select['receipt_dttm'],
    'salamt': dongjakgu_select['salamt'],
    '구': "동작구"
}
dongjakgu = DataFrame(dongjakgu)

dongjakgu = dongjakgu.rename( columns = {'receipt_dttm' : '일자'} )
dongjakgu_select_table = dongjakgu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 
dongjakgu_select_table

#영등포구
yeongdeungpogu = {
    'receipt_dttm': yeongdeungpogu_select['receipt_dttm'],
    'salamt': yeongdeungpogu_select['salamt'],
    '구': "영등포구"
}
yeongdeungpogu = DataFrame(yeongdeungpogu)

yeongdeungpogu = yeongdeungpogu.rename( columns = {'receipt_dttm' : '일자'} )
yeongdeungpogu_select_table = yeongdeungpogu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 

yeongdeungpogu_select_table

#강북구
kangbukgu = {
    'receipt_dttm': kangbukgu_select['receipt_dttm'],
    'salamt': kangbukgu_select['salamt'],
    '구': "강북구"
}
kangbukgu = DataFrame(kangbukgu)

kangbukgu = kangbukgu.rename( columns = {'receipt_dttm' : '일자'} )
kangbukgu_select_table = kangbukgu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 

kangbukgu_select_table

#성북구
sungbukgu = {
    'receipt_dttm': sungbukgu_select['receipt_dttm'],
    'salamt': sungbukgu_select['salamt'],
    '구': "성북구"
}
sungbukgu = DataFrame(sungbukgu)

sungbukgu = sungbukgu.rename( columns = {'receipt_dttm' : '일자'} )
sungbukgu_select_table = sungbukgu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 

sungbukgu_select_table

#중랑구
jungranggu = {
    'receipt_dttm': jungranggu_select['receipt_dttm'],
    'salamt': jungranggu_select['salamt'],
    '구': "중랑구"
}
jungranggu = DataFrame(jungranggu)

jungranggu = jungranggu.rename( columns = {'receipt_dttm' : '일자'} )
jungranggu_select_table = jungranggu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 

jungranggu_select_table

#동대문구
dongdaemungu = {
    'receipt_dttm': dongdaemungu_select['receipt_dttm'],
    'salamt': dongdaemungu_select['salamt'],
    '구': "동대문구"
}
dongdaemungu = DataFrame(dongdaemungu)

dongdaemungu = dongdaemungu.rename( columns = {'receipt_dttm' : '일자'} )
dongdaemungu_select_table = dongdaemungu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 

dongdaemungu_select_table

#광진구
gwangjingu = {
    'receipt_dttm': gwangjingu_select['receipt_dttm'],
    'salamt': gwangjingu_select['salamt'],
    '구': "광진구"
}
gwangjingu = DataFrame(gwangjingu)

gwangjingu = gwangjingu.rename( columns = {'receipt_dttm' : '일자'} )
gwangjingu_select_table = gwangjingu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 

gwangjingu_select_table

#성동구
sungdonggu = {
    'receipt_dttm': sungdonggu_select['receipt_dttm'],
    'salamt': sungdonggu_select['salamt'],
    '구': "성동구"
}
sungdonggu = DataFrame(sungdonggu)

sungdonggu = sungdonggu.rename( columns = {'receipt_dttm' : '일자'} )
sungdonggu_select_table = sungdonggu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 

sungdonggu_select_table

#용산구
yongsangu = {
    'receipt_dttm': yongsangu_select['receipt_dttm'],
    'salamt': yongsangu_select['salamt'],
    '구': "용산구"
}
yongsangu = DataFrame(yongsangu)

yongsangu = yongsangu.rename( columns = {'receipt_dttm' : '일자'} )
yongsangu_select_table = yongsangu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 

yongsangu_select_table

#중구
junggu = {
    'receipt_dttm': junggu_select['receipt_dttm'],
    'salamt': junggu_select['salamt'],
    '구': "중구"
}
junggu = DataFrame(junggu)

junggu = junggu.rename( columns = {'receipt_dttm' : '일자'} )
junggu_select_table = junggu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 

junggu_select_table

#종로구
jongrogu = {
    'receipt_dttm': jongrogu_select['receipt_dttm'],
    'salamt': jongrogu_select['salamt'],
    '구': "종로구"
}
jongrogu = DataFrame(jongrogu)

jongrogu = jongrogu.rename( columns = {'receipt_dttm' : '일자'} )
jongrogu_select_table = jongrogu.pivot_table(index = '일자', columns = '구', values = 'salamt', aggfunc = 'sum') 

jongrogu_select_table

table = pd.concat([kangdonggu_select_table, gemcheongu_select_table], axis=1)
table = pd.concat([table, gurogu_select_table], axis=1)
table = pd.concat([table, gangseogu_select_table], axis=1)
table = pd.concat([table, yangcheongu_select_table], axis=1)
table = pd.concat([table, seodaemungu_select_table], axis=1)
table = pd.concat([table, eunpyeonggu_select_table], axis=1)
table = pd.concat([table, nowongu_select_table], axis=1)
table = pd.concat([table, dobonggu_select_table], axis=1)
table = pd.concat([table, songpagu_select_table], axis=1)
table = pd.concat([table, gangnamgu_select_table], axis=1)
table = pd.concat([table, seochogu_select_table], axis=1)
table = pd.concat([table, gwanakgu_select_table], axis=1)
table = pd.concat([table, dongjakgu_select_table], axis=1)
table = pd.concat([table, yeongdeungpogu_select_table], axis=1)
table = pd.concat([table, kangbukgu_select_table], axis=1)
table = pd.concat([table, sungbukgu_select_table], axis=1)
table = pd.concat([table, jungranggu_select_table], axis=1)
table = pd.concat([table, dongdaemungu_select_table], axis=1)
table = pd.concat([table, gwangjingu_select_table], axis=1)
table = pd.concat([table, sungdonggu_select_table], axis=1)
table = pd.concat([table, junggu_select_table], axis=1)
table = pd.concat([table, jongrogu_select_table], axis=1)
table = pd.concat([table, mapogu_select_table], axis=1)
table = pd.concat([table, yongsangu_select_table], axis=1)


%matplotlib inline
from ipywidgets import interactive, widgets
from ipywidgets import interact, interact_manual
from IPython.display import display

import folium.plugins

import datetime

m1 = folium.Map(location = [37.5202,126.982], zoom_start = 11,tiles='Stamen Toner')
m2 = folium.Map(location = [37.5202,126.982], zoom_start = 11,tiles='Stamen Toner')

def days_between(start_dt,end_dt):
    m1 = folium.Map(location = [37.5202,126.982], zoom_start = 11,tiles='Stamen Toner')
    m2 = folium.Map(location = [37.5202,126.982], zoom_start = 11,tiles='Stamen Toner')
    # 시작일과 종료일 사이에 몇일이 있는지 계산합니다.
    #'2020-0' + str(month) + '-' + "{0:0>2}".format(str(day))
    start_day = datetime.date(2020, 1, 4)
    start_i = (start_dt - start_day).days
    end_i = (end_dt - start_day).days
    mapping_1 = float_gu[start_i:end_i+1].sum()
    mapping_2 = table[start_i:end_i+1].sum()
    
    m1.choropleth(geo_data=geo_str,data=mapping_1, columns = ['구'],fill_color='PuRd', key_on='feature.id',
                  fill_opacity=0.7,line_opacity=10,legend_name='Consume1')
    m2.choropleth(geo_data=geo_str,data=mapping_2, columns = ['구'],fill_color='BuGn', key_on='feature.id',
                  fill_opacity=0.7,line_opacity=10,legend_name='Consume2')
    display(m1)

interact(days_between,
        start_dt=widgets.DatePicker(value=datetime.date(2020,1,4)),
        end_dt=widgets.DatePicker(value=datetime.date(2020,5,31)));
        
%matplotlib inline
from ipywidgets import interactive, widgets
from ipywidgets import interact, interact_manual
from IPython.display import display

import folium.plugins

import datetime

m1 = folium.Map(location = [37.5202,126.982], zoom_start = 11,tiles='Stamen Toner')
m2 = folium.Map(location = [37.5202,126.982], zoom_start = 11,tiles='Stamen Toner')

def days_between(start_dt,end_dt):
    m1 = folium.Map(location = [37.5202,126.982], zoom_start = 11,tiles='Stamen Toner')
    m2 = folium.Map(location = [37.5202,126.982], zoom_start = 11,tiles='Stamen Toner')
    # 시작일과 종료일 사이에 몇일이 있는지 계산합니다.
    #'2020-0' + str(month) + '-' + "{0:0>2}".format(str(day))
    start_day = datetime.date(2020, 1, 4)
    start_i = (start_dt - start_day).days
    end_i = (end_dt - start_day).days
    mapping_1 = float_gu[start_i:end_i+1].sum()
    mapping_2 = table[start_i:end_i+1].sum()
    
    m1.choropleth(geo_data=geo_str,data=mapping_1, columns = ['구'],fill_color='PuRd', key_on='feature.id',
                  fill_opacity=0.7,line_opacity=10,legend_name='Consume1')
    m2.choropleth(geo_data=geo_str,data=mapping_2, columns = ['구'],fill_color='BuGn', key_on='feature.id',
                  fill_opacity=0.7,line_opacity=10,legend_name='Consume2')
    display(m2)

interact(days_between,
        start_dt=widgets.DatePicker(value=datetime.date(2020,1,4)),
        end_dt=widgets.DatePicker(value=datetime.date(2020,5,31)));
