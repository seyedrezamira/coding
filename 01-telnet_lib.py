import getpass
import telnetlib

HOST = "10.100.2.178"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write("enable\n")
tn.write("conf t\n")

print(tn.read_all().decode('ascii'))

