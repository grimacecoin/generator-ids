import urllib, urllib2
import random
#Script xYoiker
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("xYoiker Xat IDS Generator")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
print("Note: In the file 'proxies.txt' you must place the proxies to be used in the log of identifiers if you do not put proxies will not work, by default comes some proxies.\n\n")
raw_input("-> Press 'Enter' to get started <-")
def getBetween(strSource, strStart,strEnd):
    start = strSource.find(strStart) + len(strStart)
    end = strSource.find(strEnd,start)
    return strSource[start:end]
def generator_xYoik():
    while 1:
         try:
             Proxies_Exist = True
             Proxies = [i.strip() for i in open('proxies.txt','r').read().splitlines()]
             Proxies = random.choice(Proxies)
             Proxy = Proxies.split(':')
             ProxyInfo = 'https://' + str(Proxy[0]) + ':' + str(Proxy[1])
             print("---------------------------------")
             print("~[ Successfully loaded proxy ]~")
             print("---------------------------------\n")
             print("Proxy to use: " + str(Proxy[0]) + ':' + str(Proxy[1]) + "\n")
             Auser3 = urllib.urlopen('https://xat.com/web_gear/chat/auser3.php', proxies = { 'http': ProxyInfo }).read()
             Ids = open("ids.txt","a+")
             if Auser3 in Ids != False or Auser3.find('&UserId=') != False:
                 Ids.write("")
                 Ids.close()
                 generator_xYoik()
             else:
                 Ids.write(Auser3 + "\n")
                 Ids.close()
                 print("New ID: " + Auser3 + "\n")
                 generator_xYoik()
         except:
             Proxies_Exist = False
             if Proxies_Exist == False:
                 try:
                     print("--------------------------------------------------------------------------")
                     print("~[ Successfully loaded proxy from 'proxies.txt' ]~")
                     print("--------------------------------------------------------------------------")
                     print("Proxy being used: " + str(IP) + ':' + str(Port) + "\n")
                     Auser3 = urllib.urlopen('https://xat.com/web_gear/chat/auser3.php', proxies = { 'http': ProxyInfo }).read()
                     Ids = open("ids.txt","a+")
                     if Auser3 in Ids != False or Auser3.find('&UserId=') != False:
                         Ids.write("")
                         Ids.close()
                         generator_xYoik()
                     else:
                         Ids.write(Auser3 + "\n")
                         Ids.close()
                         print("New ID: " + Auser3 + "\n")
                         generator_xYoik()
                 except:
                    print("Could not connect to 'proxies.txt' ! Restarting script!'")
                    generator_xYoik()
generator_xYoik()