# To-do
# Multi Threating can speed up the process, also we can remove the MultiPing dependency we formulate our own ICMP packges.

# Import the built in socket module and MultiPing (Dependency)
import socket
from multiping import MultiPing

# Check Open Port (Socket implementaion (TCP))
def isPortOpen(ip,port=22):
    # Configure socket object (TCP)
    socketToConnect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set Connection Time Out
    socketToConnect.settimeout(5)

    for hostIp in ip:
        print('Checking port 22 on Host: {}'.format(hostIp))
        try:
            # Connecting
            socketToConnect.connect((hostIp, int(port)))
            socketToConnect.shutdown(2)
            print('Port 22 is open!!!')
            continue
        except:
            # On exception return false
            print('Timeout set to: ' + str(socketToConnect.gettimeout()) + 's')
            print('Por 22 is not open')
            continue

# Check host on network (/24)
def isHostOn():
    # Request IP Address
    hostIp = input('Whats you IP?\n')

    # Host On Python List
    onHosts = []

    # Splicing IP to determine network to be tested (/24)
    gettingNetwork = hostIp.split('.')

    # Looping through all addresses (/24) (Modify for debugging)
    for host in range(1,255):
        addressToPing = "{}.{}.{}.{}".format(gettingNetwork[0], gettingNetwork[1], gettingNetwork[2], host)
        mp = MultiPing([addressToPing])
        mp.send()
        # Set responses and 1 sec timeout
        responses, no_responses = mp.receive(1)

        if responses.keys():
            for addr, rtt in responses.items():
                # Printing to console host who responded
                print("{} responded in {}".format(addr, rtt))
                onHosts.append(addr)
    # Printing list of addresses that respondeds
    print("\n\n\n\n" + "Host on the network: {}".format(onHosts))
    return onHosts

# Script starts here
onHostsList = isHostOn()
isPortOpen(onHostsList)