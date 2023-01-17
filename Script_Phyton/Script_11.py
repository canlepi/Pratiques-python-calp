ch = "  salut tout le monde  "
print(len(ch))
ch1 = ch.strip()
print(ch1)
print(len(ch1))

ch2 = ch.lstrip()
print(ch2)
print(len(ch2))

ch3 = ch.lstrip()
print(ch3)
print(len(ch3))

ch4 = "***salut***tout***le***monde***"
print(ch4)
ch5 = ch.strip("*")
print(ch5)
print(len(ch5))
print(ch4.replace("*"," "))

ch6="SALUT TOUT le monde"
print(ch6.lower())
print(ch6.upper())

ch7="salut tout le monde le monde"
print(ch7.count("monde"))
print(ch7.startswith("salut"))
print(ch7.endswith("salut"))
ch8="un-deux-trois-quatre-cinq-six-sept-huite-neuf-dix"
print(ch8.split("-"))