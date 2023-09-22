def maiores(lista_inteiros,n):
    list.append(lista_inteiros,n)
    list.sort(lista_inteiros)
    posicao = list.index(lista_inteiros,n)
    contagem = list.count(lista_inteiros,n)
    if posicao == 1:
        return lista_inteiro[posicao+1:]
    if contagem > 1:
        return lista_inteiro[posicao+contagem+1:]