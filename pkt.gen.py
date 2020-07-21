#import logging
import random

#logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

strLoad = os.urandom(random.randint(64, 1000))

#res = [sendp(Ether()/IP(dst=str(RandIP()))/TCP()/Raw(load=strLoad), iface='enp1s0f1', verbose=False) for x in range(0, 10000)]
res = [sendp(Ether()/IP()/TCP(dport=random.randrange(1000, 60000))/Raw(load=strLoad), iface='eth1', verbose=False) for x in range(0, 1000)]
exit()
