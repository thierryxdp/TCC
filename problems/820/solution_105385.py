def posLetra(string, letra, n_ocorrencia):
    '''retorna a posição da letra na string na ocorrencia dada'''
    a=0
    p=0
    if letra not in string or str.count(string, letra) < n_ocorrencia:
        return -1
    
    else:
        while n_ocorrencia > 0:
            indice = str.find(string, letra, a)
            p=indice
            a=indice+1
            n_ocorrencia-=1
    return p