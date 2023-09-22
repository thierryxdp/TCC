def repetidos(valores):
    lista = []
listaRepetido = True
for i in range(4):
    lista.append(int(input("Numero: ")))

for i in lista:
    for j in range(2,i):
        if ((i == j) == 0):
            listaRepetido = False
            break

    if listaRepetido:
            posicao = lista.index(i)
            return("Numero %i na %i° posiçaõ" % (i, posicao + 2))
    listaRepetido = True