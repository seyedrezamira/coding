f = open("mydevices")
for line in f:
    print(line.strip())
f.close()
