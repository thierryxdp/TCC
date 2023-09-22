def posLetra(frase,letra,num):
    
    num_vezes=str.count(frase,letra)
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