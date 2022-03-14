"""
1108. Defanging an IP Address
Easy

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".



Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"



Constraints:

    The given address is a valid IPv4 address.

"""


def defanging_an_ip_address(address: str) -> str:
    if address.count('.') == 3:
        ints = [0 <= int(v) <= 255 for v in address.split('.') if v.isdigit()]
        if all(ints) and len(ints) == 4:
            return address.replace('.', '[.]')


if __name__ == '__main__':
    result = defanging_an_ip_address('255.100.50.0')
    print(result)
