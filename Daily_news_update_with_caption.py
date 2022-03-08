#News reader
import requests  #import requests module
import json # import json module
def speak(str):
    from win32com.client import Dispatch   # import pywin32  module
    speak= Dispatch("SAPI.Spvoice")
    speak.speak(str)



if __name__ == '__main__':
    speak("This program made by  Engineer Bheekha ram choudhary "
          "News of today  ....lets  begin")

    url= "https://newsapi.org/v2/top-headlines?country=in&apiKey="use your api" # used new api
    news= requests.get(url).text #
    news_dict=json.loads(news) # used json module
    print(news_dict["articles"])
    arts= news_dict['articles']
    for article  in arts :
        print(article['title'])
        speak(article['title'])
        print(article['description'])
        speak(article['description'])
        speak("Moving on to the next news ...Broadcast by Ziddi Engineer ")

    speak("thank for listening news")