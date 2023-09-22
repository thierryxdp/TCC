def insere(lista_numero, n):
    lista_com_n = lista_numero + [n]
    list.sort(lista_com_n)
    posicao_de_n = list.index(lista_com_n, n)
    resultado = lista_com_n[posicao_de_n +1:]
    vezes = resultado.count(n)
    
    if n in resultado:
        del x[:vezes]
        return resultado
    else:
        return resultado