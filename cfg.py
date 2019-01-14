
SERVER = "irc.chat.twitch.tv"
PORT = 6667
NICK = "mirage_Bot"
PASS = "xxxxxxxxxxxxxxxx"
CHAN = "xxxxxxxxxxxxxxxx"
RATE = (20/30)
offline = True
no_stream = True
game = "DD"
if(offline == True):
    CD_mid = 20
    CD_short = 10
else:
    CD_mid = 40
    CD_short = 20
if(CHAN == "xxxxxxx"):
    CD_short = 5
    CD_mid = 5


oplist = {}
