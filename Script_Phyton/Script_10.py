str1="salut tout le monde"
print(str1[3])
print(str1[0])
print(str1[18])
print(len(str1))
print(str1[-1])
print(str1[-2])
print(str1[len(str1)-1])

#Decoupage de chaine de caracteres
print(str1[0:5])
print(str1[6:10])
print(str1[11:])

str2="sabacada"
print(len(str2))
print(str2[1::2])

print(str1[1::2])
print(str1[::7])
print(str1[-4:])
print(str1[::-1])

str3="Camilo Andres"
str4="Leon"
str5=str3+" "+str4
print(str5)
print(str3,str4)

str2=str2+str2
print(str2)

for i in str2:
    print(i)

for i in enumerate(str2):
    print(i)