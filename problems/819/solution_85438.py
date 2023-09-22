lista= [2, 3, 1, 5, 1, 7, 8, 8, 9, 15, 1, 1]

qtd = len(lista)


for i in range(qtd):     

    if(lista[i]==1):
        lista.remove(lista[i])
        print("Removeu")
        print(lista)

    qtd = qtd - 1
    return