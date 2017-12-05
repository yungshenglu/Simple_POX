#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import Controller
from mininet.cli import CLI

class MyTopo(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        #s3 = self.addSwitch('s3')
        #s4 = self.addSwitch('s4')

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        self.addLink(h1, s1, bw = 1, delay = '10ms', loss = 0, max_queue_size = 1000, use_htb = True)
        self.addLink(s1, s2, bw = 1, delay = '10ms', loss = 0, max_queue_size = 1000, use_htb = True)
        #self.addLink(s1, s3, bw = 1, delay = '10ms', loss = 0, max_queue_size = 1000, use_htb = True)
        #self.addLink(s2, s4, bw = 1, delay = '10ms', loss = 0, max_queue_size = 1000, use_htb = True)
        #self.addLink(s3, s4, bw = 1, delay = '10ms', loss = 0, max_queue_size = 1000, use_htb = True)
        self.addLink(s2, h2, bw = 1, delay = '10ms', loss = 0, max_queue_size = 1000, use_htb = True)

def perfTest():
    "Create network and run simple performance test"
    topo = MyTopo()
    net = Mininet(topo = topo, link = TCLink, controller = None)
    net.addController('c0', controller = RemoteController, ip = '127.0.0.1', port = 6633)
    net.start()

    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    h1 = net.get('h1')
    h2 = net.get('h2')
    h1.setMAC("0:0:0:0:0:1")
    h2.setMAC("0:0:0:0:0:2")

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    perfTest()