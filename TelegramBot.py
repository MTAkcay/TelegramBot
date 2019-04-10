
#from pprint import pprint
import time
import telepot
from telepot.loop import MessageLoop
import sports
import random
import requests
from pyowm import OWM
from currency_converter import CurrencyConverter
def handle(msg):#yakalayıcı
    chat_id = msg['chat']['id'] ##chat id 
    command = msg['text'].split()## mesajın içeriği
    whois = msg['from']['first_name']##kayıtlı ad
    #response = bot.getUpdates()
    #pprint(response)
    ayrı=msg['text']
    print (ayrı)
    print ('Got command: %s' % command)

    if command[0] == '/rastgele':
        bot.sendMessage(chat_id, random.randint(1,100))
    elif command[0] == '/merhaba':
        bot.sendMessage(chat_id,whois+' Merhaba' )
    elif command[0] == '/mac':
        all_matches = sports.all_matches()
        football = all_matches['soccer']
        for i in football:
            bot.sendMessage(chat_id,str(i))
    elif command [0] == '/cevir':
        c = CurrencyConverter()
        money=c.convert(command[1],command[2].upper(),command[3].upper())
        bot.sendMessage(chat_id,money)
    elif command [0] == '/hava':
        owm = OWM('189e24dafb6ec8b7258944c2b4b34556')
        owm_lang= OWM(language='tr')
        observation = owm.weather_at_place(command[1])
        w = observation.get_weather()
        status=str(w.get_detailed_status())
        if status =='broken clouds':
            status='Çok Bulutlu'
        elif status =='clear sky':
            status=="Açık"
        elif status =='few clouds':
            status= 'Az Bulutlu'
        elif status =='scattered clouds':
            status='Parçalı Bulutlu'
        elif status =='shower rain':
            status='Sağanak Yağışlı'
        elif status =='rain':
            status='Yağışlı'
        elif status =='thunderstorm':
            status='Fırtınalı'
        elif status =='snow':
            status="Karlı"
        elif status =='mist':
            status='Sisli'
        

        temp=w.get_temperature('celsius')
        temp_max="En Yüksek: "+ str(temp['temp_max'])
        temp_min="En Düşük: "+ str(temp['temp_min'])
        bot.sendMessage(chat_id,"Durum: "+status)   
        bot.sendMessage(chat_id,temp_max)
        bot.sendMessage(chat_id,temp_min)
bot = telepot.Bot('850122888:AAGG6LS6CwbTWMd41uCP1PKNHTHR0MDHK8s')
## thread olarak hep mesaj yakalıyor.
MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')
#infinite loop
#while 1:
#   time.sleep(10)
