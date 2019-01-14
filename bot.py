# bot.py
import cfg
import socket
import time
import re
import utils
import random
import traceback
import sys
from datetime import datetime, tzinfo



s = socket.socket()
s.connect(("irc.chat.twitch.tv", 6667))
s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
s.send("JOIN #{}\r\n".format(cfg.CHAN).encode("utf-8"))
print("Successfully joined {}'s chatroom".format(cfg.CHAN))
cur_time = None
def chat(sock, msg):
    global cur_time
    """
    Send a chat message to the server.
    Keyword arguments:
    sock -- the socket over which to send the message
    msg  -- the message to be sent
    """
    cur_msg = "PRIVMSG #{} :{}".format(cfg.CHAN, msg).encode("utf-8")
    sock.send(cur_msg + "\r\n".encode("utf-8"))
    print("Sending message to {}'s channel".format(cfg.CHAN))
    cur_time = time.time()

def waitForMessage():
    srvResponse = s.recv(2048)
    return srvResponse.decode().split("\n")[0]

def handleMessage(srvResponse):
    global cur_time
    if "PING" in srvResponse:
        s.send("PONG tmi.twitch.tv\r\n".encode("utf-8"))
        print("PONG")

    elif "PRIVMSG" in srvResponse: 
        user = srvResponse.split(":", 2)[1].split("!", 1)[0].strip()
        message = (srvResponse.split(":", 2)[2].strip())
        if(cfg.offline == True):
            print(user + ": " + message)
        x = message.split(" ")
        if cur_time == None or (time.time() - cur_time > cfg.CD_short):
            if cfg.CHAN == "moonmoon_ow" or cfg.CHAN =="mirage1g": 
                if "peepoPooPoo" in x and user != "nightbot":
                    poop_choice = random.choice(utils.poop_response)
                    if poop_choice == utils.poop_response[2]:
                        chat(s,"peepoPooPoo Hey {} ".format(user) + poop_choice)
                    # print("xd")
                    elif poop_choice == utils.poop_response[3]:
                        chat(s,poop_choice + " {}!! HYPERROBDAB".format(user.upper()))
                        #print("xd")
                    else:
                        chat(s,"peepoPooPoo "+ poop_choice)                  
            if "robDab" in x and user != "nightbot":
                chat(s,"robDab")

            if x.count("AYAYA") >= 1 and x.count("FeelsAyayaMan") == 0:
                chat(s,"moon2PLSNO 👉 AYAYA {}".format(user))
            if(cfg.game == "DD"):
                if x.count("moon2H") >= 1 and x.count("PIT") >= 1:
                    chat(s,"THE PIT BECKONS moon2H") 
                
            if cfg.offline == True and cfg.no_stream == True:
                if x.count("no") == 1 and (x.count("stream?") == 1):
                    if x.index("no") == x.index("stream?") - 1:                      
                        #CHANGE THIS IN OFFLINE CHAT .format(username)
                        chat(s,"!title {}".format(user))
                        cur_time = time.time()
            if message == '!rps':
                chat(s,"{}? moon2T What do you play?".format(user))

            if message[:5] == '!rps ':
                randvalue = random.randrange(2)
                if randvalue == 0:
                    play = "rock"
                elif randvalue == 1:
                    play = "paper"
                else:
                    play = "scissors"
                if x[1] == "rock":
                    if play ==  "rock":
                        chat(s, "{} played {}. I play {}, no one wins moon2SHRUG".format(user, x[1], play))
                        
                    if play ==  "scissors":
                        chat(s, "{} played {}. I play {}, {} wins moon2WAH".format(user, x[1], play, user))
                    if play ==  "paper":
                        chat(s, "{} played {}. I play {}, I win moon2H".format(user, x[1], play))
                elif x[1] == "paper":
                    if play ==  "paper":
                        chat(s, "{} played {}. I play {}, no one wins moon2SHRUG".format(user, x[1], play))
                    if play ==  "rock":
                        chat(s, "{} played {}. I play {}, {} wins moon2WAH".format(user, x[1], play, user))
                    if play ==  "scissors":
                        chat(s, "{} played {}. I play {}, I win moon2H".format(user, x[1], play))
                elif x[1] == "scissors":
                    if play ==  "scissors":
                        chat(s, "{} played {}. I play {}, no one wins moon2SHRUG".format(user, x[1], play))
                    if play ==  "paper":
                        chat(s, "{} played {}. I play {}, {} wins moon2WAH".format(user, x[1], play, user))
                    if play ==  "rock":
                        chat(s, "{} played {}. I play {}, I win moon2H".format(user, x[1], play))
                else:
                    chat(s,"{}? moon2T".format(user))
                                
            if (x.count("⎝⎠") >= 2 or x.count("⎝_⎠") >= 2) and x.count("╲╱╲╱") >= 1:
                chat(s,"moon2PLSNO 👉 Weebs {}".format(user))

            if message[:len("!roll50k")] == "!roll50k":
                if user == "mirage1g":
                    chat(s,"50000")
                else:
                    chat(s,"{}".format(random.randint(1,50000)))
        else:
            print(time.time() - cur_time)
            print("The bot is on cooldown, did not chat")
        '''if message[:len(":comet: moon2DEV" )] == ':comet: moon2DEV ' or  message[:len("☄️ moon2DEV " )] == '☄️ moon2DEV ':
            if cur_time == None or (time.time() - cur_time > cfg.CD_long):
                if(cur_time != None):
                    print(time.time() - cur_time)
                cur_time = time.time()
                chat(s,"moon2D")
            else:
                print("current time is {}".format(time.time()))
                print(time.time() - cur_time)
                print("did not chat")
                 '''
                 
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
