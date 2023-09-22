def posLetra(frase,letra,ocorrencia):
    '''retorna a posição na frase da ocorrencia desejada da letra informada. str,str,int->int'''
    a=frase.count(letra)
    if a<ocorrencia:
        return -1
    a=''
    i=0
    while i<len(frase):
        if frase[i] == letra:
            a=a.replace(frase[i],'a'+str(i+1))
        i=i+1
        return a.find('a'+str(ocorrencia))