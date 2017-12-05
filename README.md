# Simple SDN on Mininet and POX controller

[![License: IEEE](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

This respository is to build a simple SDN topology on Mininet with POX controller.

## Environment Setup

* Using your own Ubuntu Machine or VM
* Install Needed Tools
    ```bash
    $ sudo apt-get update
    $ sudo apt-get install -y git vim-nox python-setuptools python-all-dev flex bison traceroute
    ```
* Install **Mininet**
    ```bash
    $ cd ~
    $ git clone git://github.com/mininet/mininet
    $ cd mininet
    $ ./util/install.sh -fnv
    ```
* Install **POX**
    ```bash
    $ cd ~
    $ git clone http://github.com/noxrepo/pox
    ```
* Install **ltprotocol**
    ```
    $ cd ~
    $ git clone git://github.com/dound/ltprotocol.git
    $ cd ltprotocol
    $ sudo python setup.py install
    ```

## Execution

* Clone this repository. If you have already installed the POX controller, just move the `simple_controller.py` under the `./pox/ext` into your POX folder `./pox/ext`.
    ```
    $ git clone https://github.com/yungshenglu/Simple_POX_SDN
    ```
* Run the `simple_controller` on POX and don't close this terminal.
    ```
    $ cd ./pox
    $ ./pox.py simple_controller
    ```
* Open another terminal and run the `simple.py` on Mininet.
    ```
    # Change the directory into the program simple.py
    # Change the mode of simple.py (Optional)
    $ sudo chmod +x simple.py
    $ sudo ./simple.py
    ```
* After running the `simple.py`, it will return some messages on the terminal.
    ```bash
    *** Creating network
    *** Adding hosts:h1 h2
    *** Adding switches:s1 s2
    *** Adding links:
    (1.00Mbit 10ms delay 0.00000% loss) (1.00Mbit 10ms delay 0.00000% loss) (h1, s1) (1.00Mbit 10ms delay 0.00000% loss)
    (1.00Mbit 10ms delay 0.00000% loss) (s1, s2) (1.00Mbit 10ms delay 0.00000% loss) (1.00Mbit 10ms delay 0.00000% loss)
    (s2, h2)
    *** Configuring hosts
    h1 h2
    Unable to contact the remote controller at 127.0.0.1:6633
    *** Starting controller
    c0
    *** Starting 2 switches
    s1 s2 ...(1.00Mbit 10ms delay 0.00000% loss) (1.00Mbit 10ms delay 0.00000% loss) (1.00Mbit 10ms delay 0.00000% loss)
    (1.00Mbit 10ms delay 0.00000% loss)
    Dumping host connections
    h1 h1-eth0:s1-eth1
    h2 h2-eth0:s2-eth2
    *** Starting CLI:
    mininet> 
    ```
* Ping the host h2 on h1
    ```bash
    # Ping with setting up the number of ICMP echo requests to send
    mininet> h1 ping -c 10 h2
    # Ping with setting up rhw TTL value
    mininet> h1 ping -i -0.1 h2
    ```
* If success, it will return the following results.
    ```bash
    ING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
    64 bytes from 10.0.0.2: icmp_seq=9 ttl=64 time=81.3 ms
    64 bytes from 10.0.0.2: icmp_seq=12 ttl=64 time=80.5 ms
    64 bytes from 10.0.0.2: icmp_seq=14 ttl=64 time=80.7 ms
    ...
    ```

## TODO

(Update soon...)

## Author

* [Yung-Sheng Lu](https://github.com/yungshenglu)

---
[![License: IEEE](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)