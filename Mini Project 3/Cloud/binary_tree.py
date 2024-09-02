from mininet.topo import Topo

class BinaryTree(Topo):
    """
    A binary tree topology with 8 hosts and 7 switches.
    h1 is connected to the leftmost leaf switch,
    and h8 is connected to the rightmost leaf switch.
    """
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Create switches s1-s7
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')

        # Create hosts h1-h8
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')

        # Connect hosts to switches
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(h5, s3)
        self.addLink(h6, s3)
        self.addLink(h7, s4)
        self.addLink(h8, s4)

        # Connect switches in a binary tree topology
        self.addLink(s1, s5)
        self.addLink(s2, s5)
        self.addLink(s3, s6)
        self.addLink(s4, s6)
        self.addLink(s6, s7)
        self.addLink(s5, s7)

topos = {'mytopo': BinaryTree}
