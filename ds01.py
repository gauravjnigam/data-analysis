# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 00:34:03 2018

@author: GauravN
"""

from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

consumer_key = '4K8uFtksTmjtDKKVC9p5P5H5x'
consumer_secret = 'G9RqcXBS4nmbR3ZM4lqCe3zmHh86u0hrRgY0ac3ZDRpPDpMwoQ'
access_token = '86063644-3pt9tkO2hNDIKfbGm1mM4BZu8sgkytou4hI9cOz0r'
access_token_secret = 'dXJGPd7ypzUtOyDkYlxmpBVvjKGSYrOPePJg49911enJI'

auth = OAuthHandler(consumer_key,consumer_secret);

auth.set_access_token(access_token,access_token_secret);

class PrintListner(StreamListener):
    def on_status(self, status):
        if not status.text[3] == 'RT ':
            print(status.text)
            print(status.author)

def print_to_terminal():
    listner = PrintListner()
    stream = Stream(auth,listner)
    languages = ('en',)
    stream.sample(languages=languages);
    
if __name__ == '__main__':
    print_to_terminal()

