#import logging
import random

#logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

#strLoad = os.urandom(random.randint(64, 1000))
strLoad = os.urandom(65535)

#res = [sendp(Ether()/IP(dst=str(RandIP()))/TCP()/Raw(load=strLoad), iface='enp1s0f1', verbose=False) for x in range(0, 10000)]
#res = [sendp(Ether()/IP(dst=str(RandIP()))/TCP(dport=random.randrange(1000, 60000))/Raw(load=strLoad), iface='eth1', verbose=False) for x in range(0, 1000)]
writer = PcapWriter('test1234.pcap')

for i in range(1, 10001):
    pkt = Ether()/IP(dst=str(RandIP()))/TCP(dport=random.randrange(1000, 60000))/Raw(load=os.urandom(9000))
    writer.write(pkt)

writer.close()

exit()
