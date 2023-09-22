def posLetra(frase,letra,numero):
    '''Função retorna em qual posição na frase dada letra e ocorrência;
    str,str,int->int'''
    posic = 0
    indice = 0

    while indice<numero:
        if frase.count(letra)< numero:
            return -1
        else:
            posic = frase.find(letra,posic+1)
        
        indice +=1

    return posic