# bot.py
import cfg
import socket
import time
import re
import utils, random
import commands
import traceback
import sys
from datetime import datetime, tzinfo
import requests
import json
import gta

class cmd():
    def __init__(self, cooldown):
        self.cooldown = float(cooldown)
        self.last_time_usage = 0.0
    def update_time(self):
        self.last_time_usage = time.time()
        return
    def on_cooldown(self):
        return (time.time() - self.last_time_usage) <= self.cooldown
    def get_cooldown(self):
        if self.on_cooldown() == True:
            print("This is on cooldown for {:.2f} more seconds".format(self.cooldown - (time.time() - self.last_time_usage)))
            return
def get_moderators():
    json_data = requests.get("http://tmi.twitch.tv/group/user/{}/chatters".format(cfg.CHAN))
    json_data = json_data.content.decode("utf-8")
    json_dict = json.loads(json_data)
    mod_list = json_dict["chatters"]["moderators"]
    mod_list.append(cfg.CHAN)
    return mod_list
## initialize objects for each command

rps = cmd(cfg.CD_short)
poop = cmd(cfg.CD_short)
robDab = cmd(cfg.CD_mid)
ayaya = cmd(cfg.CD_short)
pit = cmd(cfg.CD_mid)
weeb = cmd(cfg.CD_short)
dice = cmd(5)
gtabars = cmd(10)
gta_cmd = cmd(10)

s = socket.socket()
tag_count = 0
roulette_count = 0
utils.join_chan(s,cfg.SERVER,cfg.PORT,cfg.PASS,cfg.NICK,cfg.CHAN)
modlist = get_moderators()
if "mirage_bot" in modlist:
    mod_status = True
else:
    mod_status = False

def waitForMessage():
    srvResponse = s.recv(2048)
    return srvResponse.decode().split("\n")[0]

def handleMessage(srvResponse):
    if "PING" in srvResponse:
        s.send("PONG tmi.twitch.tv\r\n".encode("utf-8"))
        print("PONG")
    elif "PRIVMSG" in srvResponse: 
        user = srvResponse.split(":", 2)[1].split("!", 1)[0].strip()
        message = (srvResponse.split(":", 2)[2].strip())
        if(cfg.offline == True):
            print(user + ": " + message)
        x = message.split(" ")
        global tag_count
        global roulette_count
        
        if cfg.shit_posting == True:
            if cfg.CHAN == "xxxxxxx" or cfg.CHAN =="xxxxxxx": 
                if "peepoT" in x and user != "nightbot":
                    if poop.on_cooldown() == False:
                        poop_choice = random.choice(utils.poop_response)
                        utils.chat(s,"peepoT "+ poop_choice)  
                        poop.update_time()
                    else: 
                        poop.get_cooldown()
                if "robDab" in x and user != "nightbot":
                    if robDab.on_cooldown() == False:
                        utils.chat(s,"robDab")
                        robDab.last_time_usage = time.time()
                    else:
                        robDab.get_cooldown()
                if x.count("AYAYA") >= cfg.AY_count and x.count("FeelsAyayaMan") == 0:
                    if ayaya.on_cooldown() == False:
                        ayaya.update_time()
                        utils.chat(s,"FeelsAyayaMan 👉 AYAYA")
                    else:
                        ayaya.get_cooldown()
                
                if(cfg.game == "DD"):
                    if x.count("moon2H") >= 1 and x.count("PIT") >= 1:
                        if pit.on_cooldown == False:
                            utils.chat(s,"THE PIT BECKONS moon2H") 
                            pit.update_time()
                        else: 
                            pit.get_cooldown()
                if cfg.offline == True and cfg.no_stream == True:
                    if x.count("no") == 1 and (x.count("stream?") == 1):
                        if x.index("no") == x.index("stream?") - 1:                      
                            #CHANGE THIS IN OFFLINE CHAT .format(username)
                            utils.chat(s,"!title {}".format(user))
                if (x.count("⎝⎠") >= 2 or x.count("⎝_⎠") >= 2) and x.count("╲╱╲╱") >= 1:
                    if weeb.get_cooldown == False:
                        weeb.update_time()
                        utils.chat(s,"FeelsAyayaMan 👉 Weebs")
                    else:
                        weeb.get_cooldown()
                        if message == '!rps':
                            if rps.on_cooldown() == False:
                                rps.update_time()
                                utils.chat(s,"{}? :) What do you play?".format(user))
                            else:
                                rps.get_cooldown()
                        if message[:5] == '!rps ':
                            if rps.on_cooldown() == False:
                                rps.update_time()
                                randvalue = random.randrange(2)
                                if randvalue == 0:
                                    play = "rock"
                                elif randvalue == 1:
                                    play = "paper"
                                else:
                                    play = "scissors"
                                if x[1] == "rock":
                                    if play ==  "rock":
                                        utils.chat(s, "{} played {}. I play {}, no one wins :)".format(user, x[1], play))
                                        
                                    if play ==  "scissors":
                                        utils.chat(s, "{} played {}. I play {}, {} wins :)".format(user, x[1], play, user))
                                    if play ==  "paper":
                                        utils.chat(s, "{} played {}. I play {}, I win :)".format(user, x[1], play))
                                elif x[1] == "paper":
                                    if play ==  "paper":
                                        utils.chat(s, "{} played {}. I play {}, no one wins :)".format(user, x[1], play))
                                    if play ==  "rock":
                                        utils.chat(s, "{} played {}. I play {}, {} wins :(".format(user, x[1], play, user))
                                    if play ==  "scissors":
                                        utils.chat(s, "{} played {}. I play {}, I win :)".format(user, x[1], play))
                                elif x[1] == "scissors":
                                    if play ==  "scissors":
                                        utils.chat(s, "{} played {}. I play {}, no one wins :)".format(user, x[1], play))
                                    if play ==  "paper":
                                        utils.chat(s, "{} played {}. I play {}, {} wins :(".format(user, x[1], play, user))
                                    if play ==  "rock":
                                        utils.chat(s, "{} played {}. I play {}, I win :)".format(user, x[1], play))
                                else:
                                    utils.chat(s,"{}? :)".format(user))
                            else:
                                rps.get_cooldown()  
        if x[0] == "!gtaroll":
            if dice.on_cooldown() == False:
                dice_roll = gta.roll_dice()
                dice.update_time()
                utils.chat(s,"{} {}".format(user,dice_roll))      
            else:
                dice.get_cooldown() 
        if "!wolldatshit" == x[0]:
            if dice.on_cooldown() == False:
                dice_roll = gta.roll_dice(3,2)
                dice.update_time()
                utils.chat(s,"{} {} :)".format(user,dice_roll))      
            else:
                dice.get_cooldown()  
    
        if cfg.collect_data == True:
            if ("@" + cfg.CHAN.upper()) in x or cfg.CHAN.upper() in x:
                tag_count += 1
            if message[:len("!tagcount")] == "!tagcount":
                utils.chat(s,"/w {} {} has been tagged {} times during the current session".format(user, cfg.CHAN, tag_count))
            if "!roulette" in x:
                roulette_count += 1
            if message[:len("!roulettecount")] == "!roulettecount":
                utils.chat(s,"/w {} !roulette has been used {} times during the current session".format(user, roulette_count))
                """  if message[:len("!chats")] == "!chats":
                if ass.on_cooldown() == False:
                    ass.update_time()
                    utils.get_chatters(s,cfg.CHAN) 
                else:
                    ass.get_cooldown()  
                    """   
        if cfg.game == "GTA V RP":
            if "!gtabars" == x[0]:
                if gtabars.on_cooldown() == False:
                    gtabars.update_time()
                    utils.chat(s,"{}, From left to right: Food; Water; Oxygen; Voice chat range; Stress".format(user))      
                else:
                    gtabars.get_cooldown()  
            if "!bluemarker" == x[0]:
                if gtabars.on_cooldown() == False:
                    gtabars.update_time()
                    utils.chat(s,"{}, blue marker = bugged house marker".format(user))      
                else:
                    gtabars.get_cooldown()  

            if "!payout" == x[0] and user == "egarim_a":
                if gta_cmd.on_cooldown() == False:
                    gta_cmd.update_time()
                    try: 
                        payout_output = gta.payout(x[1],x[2],x[3])
                        if payout_output[1] == 0:
                            utils.chat(s,"{}, The person gets {}k.".format(user,payout_output[0]))
                        else:
                            utils.chat(s,"{}, The supplier of thermite gets: {}k, and the rest get: {}k".format(user,payout_output[0], payout_output[1]))        
                    except:
                        utils.chat(s,"{}, !payout <num_people> <num_vg> <num_thermite>".format(user))
                else:
                    gta_cmd.get_cooldown()       
       
       
       
        if mod_status == True:
            if x[0] == "!ban":
                if user in modlist:
                    try:
                        utils.chat(s,"/timeout {} {}".format(x[1],x[2]))
                    except:
                        utils.chat(s,"/ban {}".format(x[1]))
            for word in x:
                if word in utils.ban_list:
                    print(word)
                    utils.chat(s,"/timeout {} {}".format(user,10))
while True:
    try:
        srvResponse = waitForMessage()
        handleMessage(srvResponse)
        if srvResponse == "":
            pass

    except KeyboardInterrupt:
        s.close()
        sys.exit("\nSocket cleaned\n")

    except:
        traceback.print_exc()
