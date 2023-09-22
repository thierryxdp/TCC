def posLetra(string,letra,numero):
    '''a partir de uma string,uma letra e um número que indica a ocorrencia desejada da letra, indica em que posição da string a letra está
str,str,int-->int'''
    i=0
    ocorrencia=[]
    while len(string)>i:
        if str.find(string,letra)==-1:
            return -1
        elif string[i]==letra:
            ocorrencia += [i]
        i+=1
    if len(ocorrencia)<numero:
        return -1
    else:
        return ocorrencia[numero-1]