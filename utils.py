#utils.py
#this py file will hold all the generic socket commands that are needed to send messages and what now
import cfg


poop_response = ["me poop hehe" , "poop hehe", "it's my turn","EPIC POOP",
"HNNNNG", "hehe poop", "*plop*", "*splash*"]

def chat(sock, msg):
    """
    Send a chat message to the server.
    Keyword arguments:
    sock -- the socket over which to send the message
    msg  -- the message to be sent
    """
    cur_msg = "PRIVMSG #{} :{}".format(cfg.CHAN, msg).encode("utf-8")
    sock.send(cur_msg + "\r\n".encode("utf-8"))
if cfg.CHAN == "mirage1g":
    def ban(sock, user):
        """
        Ban a user from the current channel.
        Keyword arguments:
        sock -- the socket over which to send the ban command
        user -- the user to be banned
        """
        chat(sock, ".ban {}".format(user))

    def timeout(sock, user, secs=600):
        """
        Time out a user for a set period of time.
        Keyword arguments:
        sock -- the socket over which to send the timeout command
        user -- the user to be timed out
        secs -- the length of the timeout in seconds (default 600)
        """
        chat(sock, ".timeout {} {}".format(user, secs))

        