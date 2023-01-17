def parite(nombre):
    '''Cette fonction permet de veriifer la parite dun nombre'''
    if nombre % 2 == 0:
        print("le nombre est pair")
    else:
        print("le nombre est impair")

parite(6)
parite(7)
print(parite.__doc__)

