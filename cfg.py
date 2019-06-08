
SERVER = "irc.chat.twitch.tv"
PORT = 6667
NICK = "mirage_Bot"
PASS = "xxxxxxxxxxxxxxxx"
CHAN = "xxxxxxxxxxxxxxxx"
offline = True
no_stream = True

offline = True
no_stream = True
shit_posting = False
game = "FF"
collect_data = False

if(offline == True):
    CD_mid = 20
    CD_short = 10
    AY_count = 2
else:
    CD_mid = 40
    AY_count = 3
    CD_short = 20
if(CHAN == "egarim_a"):
    CD_short = 5
    CD_mid = 5
