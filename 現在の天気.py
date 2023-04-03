import certifi 
import requests
import json
import geocoder
import datetime
import pytz

# 現在の日付を取得
now = datetime.datetime.now()

g = geocoder.ip('me')
if g.latlng:
    lat, lon = g.latlng
    
    # 現在地の詳細な地名を取得
    location = geocoder.reverse((lat, lon), language='ja')
    
    # 詳細な地名が存在する場合のみ表示する
    if location is not None:
        address = location.address
    else:
        address = '不明'
    
    # 簡略な地名を取得
    location_simple = g.city + ', ' + g.state + ', ' + g.country
    
    # 日付を含めたURLを生成
    url = f'http://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&current_weather=true&date={now.strftime("%Y-%m-%d")}'
    
    response = requests.get(url, verify=certifi.where())
    data = json.loads(response.text)

    current_time_utc = datetime.datetime.strptime(data['current_weather']['time'], '%Y-%m-%dT%H:%M')
    jst = pytz.timezone('Asia/Tokyo')
    current_time_jst = jst.fromutc(current_time_utc).strftime("%Y-%m-%d %H:%M:%S")

    current_temp = data['current_weather']['temperature']
    weather_code = data['current_weather']['weathercode']
    wind_speed = data['current_weather']['windspeed']
    wind_direction = data['current_weather']['winddirection']

    print("詳細な現在地: ", address)
    print("簡略な現在地: ", location_simple)
    print("現在時刻 (JST): ", current_time_jst)
    print("現在気温: ", current_temp, "°C")
    print("天気コード: ", weather_code)
    print("風速: ", wind_speed, "km/h")
    print("風向: ", wind_direction, "°")
    if weather_code == 200:
        print("雷雨が予想されます。")
    elif weather_code == 201:
        print("雷雨が予想され、強い雨が降る可能性があります。")
    elif weather_code == 202:
        print("雷雨が予想され、非常に強い雨が降る可能性があります。")
    elif weather_code == 230:
        print("小雨と雷雨が予想されます。")
    elif weather_code == 231:
        print("雨と雷雨が予想されます。")
    elif weather_code == 232:
        print("大雨と雷雨が予想されます。")
    elif weather_code == 300:
        print("弱い霧が予想されます。")
    elif weather_code == 301:
        print("霧が予想されます。")
    elif weather_code == 302:
        print("濃い霧が予想されます。")
    elif weather_code == 500:
        print("小雨が予想されます。")
    elif weather_code == 501:
        print("雨が予想されます。")
    elif weather_code == 502:
        print("大雨が予想されます。")
    elif weather_code == 511:
        print("着氷性の雨が予想されます。")
    elif weather_code == 520:
        print("弱いにわか雨が予想されます。")
    elif weather_code == 521:
        print("にわか雨が予想されます。")
    elif weather_code == 522:
        print("強いにわか雨が予想されます。")
    else:
        print("天気コード: ", weather_code)

else:
    print('現在地の取得に失敗しました')
    
    
    
