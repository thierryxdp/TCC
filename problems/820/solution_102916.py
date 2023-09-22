def posLetra(frase,letra,numero):
    ''' Função retorna posição da letra desejada. atr,atr,int --->int'''
    palavras = list(frase)
    i = 0
    ocorrencias = 0
    while len(palavras) > i:
        if letra in palavras[i]:
            ocorrencias += 1
            
            if ocorrencias == numero:
                return i 
        
        i += 1
    if ocorrencias < numero:
        return -1
    else:
        return ocorrencias