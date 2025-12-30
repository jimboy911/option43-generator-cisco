import ipaddress #imports the IP address module

final_hex_address = "" #declares this variable as an empty string to put strings in later
cisco_prefix = 'f1' #the Option43 string for a Cisco WLC always starts off with these two characters
ip_count = ['04', '08', '0c'] #04 for one IP, 08 for two IPs, and 0c for three IPs (hex values)
ip_address_str = input("Please Enter the IP Address you want to convert: ") #prompts the user for IP address(es)

ip_addresses = ip_address_str.split(",") #splits each IP address into a list of strings
ip_count_index = len(ip_addresses) - 1 #sets an index number to determin which hex value to use for the IP count portion of the Option43 string

#for loop that goes through each IP address and puts together the IP address portion of the Option43 string
for each_address in ip_addresses:
    ip_object = ipaddress.IPv4Address(each_address) #uses the ipaddress module to an "ip address object" so it can be converted in the next line
    hex_address = format(ip_object, 'X') #converts the IP address to a hex string
    print(f"IP Address {ip_addresses.index(each_address) + 1}: {each_address}") #prints out the IP address to the terminal
    final_hex_address += hex_address.lower() #puts together the IP address portion of Option43 string

final_option43 = cisco_prefix + ip_count[ip_count_index] + final_hex_address #puts together the entire Option43 string.
print(f"Option43: {final_option43}") #prints out the full Option43 value to the terminal