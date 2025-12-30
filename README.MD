This automation creations Option43 values for Cisco Wireless LAN Controllers (WLC) when configuring a management subnet in Bluecat, either for a new network deployment or to update the Option43 configuration because of a controller change.


This automation can also take an Option43 value and calculate the IP address (or addresses) in order to verify which controllers the APs are likely to connect to.


To run, download this folder to a folder on your workstation.  You must have Python installed, however, there are no modules or special environments to setup.


To generate an Option43 value: ``` py option43.py ```

You will be prompted to enter an IP address.  You can enter multiple IP addresses separated by commas (do not include spaces) if you want to configure a secondary or tertiary WLC.

To "decode" or "reverse" an Option43 value: ``` py reverse_option43.py ```

You will be prompted to enter an Option43 string, it can contain colons (but no spaces).  It should print out the IP address (or addresses) of the WLC(s) contained in the string.