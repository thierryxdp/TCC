def posLetra(texto,letra,numero):
    """funcao que dado um texto, uma letra e um numero retorna a posicao da letra"""
    """str,str,int->str"""
    ocorrencia = str.count(texto, letra)
    i = 0
    lista = []
    if numero > ocorrencia:
        return -1
    else:
        while i < len(texto):
            if texto[i]==letra:
                list.append(lista, i)
            i = i + 1
        return lista[ocorrencia]