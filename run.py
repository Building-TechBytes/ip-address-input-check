#Collect input from user and verify it is a valid IP address.
import ipaddress
def validate_ip_address(ip_string):
   try:
       ip_object = ipaddress.ip_address(ip_string)
       return ip_object
   except ValueError:
       ip_object = "invalid"
       return ip_object

def valid_ip(prompt):
    while True:
        lan_ip=validate_ip_address(input(f"{prompt}:"))
        if lan_ip == "invalid":
            print("Enter a valid IPv4!")
        else:
            return lan_ip
            break
            
lan_user_ip=valid_ip("Enter user int IP")
wan_ip=valid_ip("Enter WAN IP")
