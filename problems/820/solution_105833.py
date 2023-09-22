def posLetra(string,letra,n):
    '''Retorna a posicao da ocorrencia da letra desejada na string de entrada;str,str,int->int'''
    i=0
    ocorrencia=0
    
    while i<len(string):
        x=str.find(string,letra)
        ocorrencia=ocorrencia+x
        i=i+1
    return ocorrencia