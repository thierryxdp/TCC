def posLetra(frase,letra,num):
    """Dada uma frase, uma letra e um número n, respectivamente, a função retorna o índice da n-ésima aparição da letra na frase (Caso exista menos ocorrências da letra que a ocorrência pedida, a função retorna -1); str, str, int -> int"""
    num_vezes = str.count(frase,letra)
    posicao = 0
    lista = []
    
    if num_vezes >= num:
        while posicao < len(frase):
            if frase[posicao] == letra:
                list.append(lista,posicao)
            posicao = posicao + 1
            
        return lista[num-1]
    else:
        return -1