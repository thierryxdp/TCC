def posLetra(frase,letra,numero):
    '''Retorna a posição da letra da seguinte ocorrencia desejada;
    str,str,int->int'''
    
    i=0
    ocorrencia=0
    x=str.count(frase,letra)
    if x<numero:
        return -1
    while ocorrencia<numero:
        if frase[i]==letra:
            ocorrencia+=1
        i+=1
    return i-1