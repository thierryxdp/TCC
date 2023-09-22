def posLetra(string,letra,num_ocorrencia):
    '''função que recebe como entrada uma string, uma letra, e um 
    número que indica a ocorrência desejada da letra (1 para 
    primeira ocorrência, 2 para segunda, etc). Sua função deve
    retornar em que posição da string aquela ocorrência da letra está.
    Caso exista menos ocorrências da letra do que a ocorrência
    pedida, a função deve retornar -1. str,str,int->int'''
    i=0
    resposta=-1
    while i<len(string):
        if string[i]==letra and str.count(string,letra,0,1+i)==num_ocorrencia:
            resposta=i
        i+=1
    return resposta