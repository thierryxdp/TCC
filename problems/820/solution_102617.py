def posLetra(frase,letra,ocorrencia):
    '''função que dada uma string, letra e um numero que indica
    a ocorrencia desejada da letra, retorna em que posição da
    string aquela ocorrência da letra esta   ent-> str,str,int
    saida-> int'''
    
    indice = 0
    frase2 = frase.split()
    frase3 = frase.split(letra)
    
    while indice < len(frase2):
        if list.count(frase2, letra) < ocorrencia:
            return -1
    return frase3