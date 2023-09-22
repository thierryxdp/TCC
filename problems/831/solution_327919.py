def lingua_p(frase):
    lista = frase.split(" ")
    nova = ["" for n in range(0, len(lista))]
    for i in range(0, len(lista)):
        for j in range(0, len(lista[i])):
            if j % 2 == 1:
                nova[i] += lista[i][j]

    return ' '.join(nova)