def posLetra(frase,letra,num):
    '''Retorna a posição da letra no número de ocorrência 
    em função da entrada; recebe como parâmetro uma frase,
    uma letra e o número de ocorrência do caractér. String,
    String,Int-->Int'''
    i=0
    ocorrencia=0
    while i<len(frase):
        if(frase[i]==letra):
            ocorrencia+=1
        i=i+1
    if ocorrencia<num:
        return -1
    else:
        pos=str.index(frase,letra,frase[i])
        return pos