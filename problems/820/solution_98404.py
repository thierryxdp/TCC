def posLetra(palavra,letra,aparicao):
    """funcao que dado um texto, uma letra e um numero retorna a posicao da letra"""
    """str,str,int->str"""
    n_ocorrencias=str.count(palavra,letra)
    indices=[]
    contador=0

    if aparicao > n_ocorrencias:
        return -1
    else:
        while contador < len(palavra):
            if palavra[contador]==letra:
                list.append(indices,contador)
            contador = contador+1
        return indices[aparicao-1]