import ipaddress #imports the IP address module

cisco_prefix = 'f1' #the Option43 string for a Cisco WLC always starts off with these two characters
ip_count = ['04', '08', '0c'] #04 for one IP, 08 for two IPs, and 0c for three IPs (hex values)
option43_str = input("Please Enter the Option43 string you want to reverse: ") #prompts user for the Option43 string

option43_str_filtered = option43_str.replace(":", "") #removes any colons in the Option43 string
print(f"Option43: {option43_str_filtered}") #prints out the Option43 string to the terminal for confirmation

number_of_ips_hex = option43_str_filtered[2:4] #checks the values of the 3rd and 4th character (starts at the 2nd index and stops before the 4th index)
ips_hex = option43_str_filtered[4:] #this separates out the IP addresses from the rest of the Option43 string.

number_of_ips_int = ip_count.index(number_of_ips_hex) + 1 #this is an integer
print(f"Number of IPs: {number_of_ips_int}") #shows the number IP addresses in the Option43 string.

n = 0 #sets a counter for the while loop, designed to count up

#while loop that goes through each IP address and prints it out
while number_of_ips_int != 0:
    first_position = 8*n #creates a start value for the slicer in order to correctly get the hex characters of the IP address as it iterates through each IP address
    last_position = 8*n + 8 #creates an end value for the slicer in order to correctly get the hex characters of the IP address as it iterates through each IP address
    ip_address_hex = ips_hex[first_position:last_position] #grabs the IP address in hex format
    ip_address = ipaddress.IPv4Address(int(ip_address_hex, 16)) #converts the IP address to the dotted-decimal format
    print(f"IP Address {n+1}: {ip_address}") #prints out the IP address of the WLC to the terminal
    number_of_ips_int -= 1 #this iterates to the next WLC IP address, if it exists
    n += 1 #this iterates the n count up by 1