import requests
import time
import random
import datetime
from colorama import init
init()
from colorama import Fore, Back, Style
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import names



client=Bot('.')
@client.command()
async def arbys(catchall,acc_num):
    #example .arbys email.space 3
    s = requests.Session()

    for x in range (0,int(acc_num)):
    #Take out the "#" is you wanna use proxies. You don't need both HTTP and HTTPS proxies. One of either type will work
    #proxies = { 
        #"http"  : "http://10.10.1.10:3128", 
        #"https" : "https://10.10.1.11:1080"   
    #}
            
        random_catchall = str(random.randint(1,99999999999999999999999999)) + '@' + catchall
        extra_headers = {
        "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        "Accept-Encoding": 'gzip, deflate, br',
        'Accept-Language': 'en,en-US;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '237',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'arbys.fbmta.com',
        'Origin': 'https://arbys.com',
        'Pragma': 'no-cache',
        'Referer': 'https://arbys.com/get-deals',
        'Upgrade-Insecure-Requests': '1',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        }
    
    
        payload = {
        "ListID": "27917287443",
        "SiteGUID": "220b8a14-335c-42e0-8b07-1dfe8ec259cd",
        '_Theme': "27917287575",
        'InputSource': "W-Mobile",
        'Birthdate': "",
        "FirstName": names.get_first_name(),
        'LastName': names.get_last_name(),
        'EmailAddress': random_catchall,
        'Zip': "",
        'StoreCode': "",
        'DOBM': "",
        'DOBD': "",
        "OverThirteen": "True",
        "MobilePhone":  "",
        }

        rr = s.post("https://arbys.fbmta.com/members/subscribe.aspx",headers = extra_headers, data = payload)
        # use this one if your using proxies. Remove the other line: rr = s.post("https://arbys.fbmta.com/members/subscribe.aspx",headers = extra_headers, data = payload,proxies = proxies)
        await client.say('Signed up using ' + random_catchall + ' as email address. Check your email for the code')    
client.run('Your Token Here')
