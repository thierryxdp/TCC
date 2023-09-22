def posLetra(stringI, letra,num):
    """Calcula e retorna a posicao da string em que a 
    ocorrencia(num) desejada da letra em uma string esta;
    str,str,int-->int"""
    i=0
    ocorrencia=-1
    while i < len(stringI) and str.count(stringI,letra)==num :
        if stringI[i] == letra:
            ocorrencia = (str.index(stringI,letra,i))
        i=i+1
    return ocorrencia