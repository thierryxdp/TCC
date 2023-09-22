def posLetra(frase,letra,ocorrencia):
    '''função que dada uma string, letra e um numero que indica
    a ocorrencia desejada da letra, retorna em que posição da
    string aquela ocorrência da letra esta   ent-> str,str,int
    saida-> int'''
    
    indice = 0
    frase2 = frase.split()
    
    while indice < len(frase2):
        if list.count(lista2, letra) < ocorrencia:
            return -1