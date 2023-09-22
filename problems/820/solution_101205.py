def posletra(x,y,z):
    '''função que retorna a posição na string em que a ocorrencia desejada,z, de letra,y, se encontra na frase,x,retornando menos 1 caso não haja ocorrência da letra'''
     if x.count(y) < z:
        return -1
    else:
        i = 0
        let = []
        caract = list(x)
        while i < len(caract) and len(let) < z:
            if y == caract[i]:
                list.append(y, caract[i])
            i = i + 1
        return i - 1