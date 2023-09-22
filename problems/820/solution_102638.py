def posLetra(frase,letra,ocorrencia):
    ''' função que dada uma frase, letra e um numero que 
    indica a ocorrencia desejada da letra, retorna em 
    que posicao da frase esta aquela ocorrencia 
    ent-> (str,str,int)  saida-> int '''
    
    frase2 = list(frase)
    indice = 0
    
    if ocorrencia == 1:
        return list.index(frase2,letra)
    if list.count(frase2,letra) < ocorrencia:
        return -1
    frase3 = frase.split(letra)
    frase4 = ''.join(frase3)
    return frase3