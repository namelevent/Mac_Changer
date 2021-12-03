import subprocess
import optparse
import re

def parse():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change")
    parse_object.add_option("-m","--mac",dest="mac_address",help="New mac address")
    return parse_object.parse_args()

def change_mac_address(interface,mac_address):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
    subprocess.call(["ifconfig",interface,"up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None

(user_input,arguments) = parse()

change_mac_address(user_input.interface,user_input.mac_address)
finaly_mac = control_new_mac(str(user_input.interface))
if finaly_mac == user_input.mac_address:
    print("Mac Changed ...")
else:
    print("Mac Not Change!!")