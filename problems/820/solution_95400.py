def posLetra(frase,letra,num):
    """Dada uma string, uma letra e um numero de ocorrencia, retorna em que posicao ocorreu a ocorrencia determinada pelo parametro "num" """
    """entrada: str,str,int
    saida: int"""
    
    pos=0
    acumulador=0
    
    while po < len(frase):
        if str.count(frase,letra)>=num:
            if letra == frase[pos]:
                acumulador = frase.index(letra)
        
        else:
            acumulador = -1
        
        pos = pos+1
    
    return acumulador