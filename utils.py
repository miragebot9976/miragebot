#utils.py
#this py file will hold all the generic socket commands that are needed to send messages and what now
import cfg
import time
import datetime
import bot


poop_response = ["me poop hehe" , "poop hehe",
"HNNNNG", "hehe poop", "*plop*", "*splash*"]
ban_list = []
timeout_list = ["Kappa"]

def chat(sock, msg):
    cur_msg = "PRIVMSG #{} :{}".format(cfg.CHAN, msg).encode("utf-8")
    sock.send(cur_msg + "\r\n".encode("utf-8"))
    print("Sent message to {}'s channel".format(cfg.CHAN))
def join_chan(sock,server,port,PASS,NICK,CHAN):
    sock.connect((server, port))
    sock.send("PASS {}\r\n".format(PASS).encode("utf-8"))
    sock.send("NICK {}\r\n".format(NICK).encode("utf-8"))
    sock.send("JOIN #{}\r\n".format(CHAN).encode("utf-8"))
    if bot.mod_status == True:
        sock.send("CAP REQ :twitch.tv/membership\r\n".encode("utf-8"))
        sock.send("CAP REQ :twitch.tv/commands\r\n".encode("utf-8"))
        #sock.send("CAP REQ :twitch.tv/tags\r\n".encode("utf-8"))
    print("Successfully joined {}'s chatroom".format(CHAN))
#def pubsub_connect(sock,pubsub,)
if cfg.CHAN == "egarim_a":
    def ban(sock, user):
        chat(sock, ".ban {}".format(user))

    def timeout(sock, user, secs=600):
        chat(sock, ".timeout {} {}".format(user, secs))

        

    