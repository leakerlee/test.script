#import logging
import random

#logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

strLoad = os.urandom(random.randint(64, 65535))

res = [sendp(Ether()/IP(dst=str(RandIP()))/TCP()/Raw(load=strLoad), iface='enp1s0f1', verbose=False) for x in range(0, 10000)]
exit()

