def freq_palavras (frase):
    '''
    Função que recebe uma frase e retorna um dicionario
    contendo as palavras da frase e suas frequencias
    string---> dicionario
    '''
    frasec=str.split(frase)
    n=0
    dicionario={}
    while n<len(frasec):
        num=str.count(frase,frasec[n])
        palavra=frasec[n]
        dicionario[palavra]=num
        n+=1
    return dicionario