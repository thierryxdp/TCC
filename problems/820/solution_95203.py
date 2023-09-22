def posLetra(frase,letra,num):
    """Dada uma string, uma letra e um numero de ocorrencia, retorna em que posicao aparece a letra na frase de acordo com o numero de sua ocorrencia"""
    """entrada: str,str,int
    saida: int"""
    
    pos = 0
    acumulador = 0
    
    while pos < len(frase):
        if str.count(frase,letra) >= num:
            if letra = frase[pos]:
                acumulador = frase.index(letra)
        pos = pos +1
        
        elif str.count(frase,letra) < num:
            acumulador = -1
            
    return acumulador