def insere(lista_num,n):
    lista_num.append(n)
    lista_num.sort()
    return lista_num

def maiores(numeros,numero):
    crescente =insere(numeros,numero)
    posicao = crescente.index(numero)
    del crescente[0:posicao+1]
    return crescente