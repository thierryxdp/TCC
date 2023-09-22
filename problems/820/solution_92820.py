def posLetra(frase,letra,n):
    '''posLetra recebe uma list, uma letra e um numero
    inteiro e devolve um numero inteiro
    determina os multiplos de n numa determinada lista 
    str, str, int --> int'''
    quant_letras=str.count(frase,letra)
    
    if n>quant_letras:
        return -1
    
    contador=0
    existencia=0
    
    while existencia!=n:
        if frase[contador]==letra:
            existencia+=1
            contador+=1
        else:
            contador+=1
            
    return contador-1