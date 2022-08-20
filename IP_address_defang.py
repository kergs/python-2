import ipaddress
from tkinter.ttk import Separator


def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    Separator = "[.]"
    new_address = Separator.join(split_address)
    return new_address

print("Enter IP address")
ipadd = input(":>> ")
ipaddress = ip_address(ipadd)
print(ipaddress)