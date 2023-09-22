def freq_palavras(frases):
    '''recebe uma string e retorna um dicionario com cada palavra uma chave
    com o valor sendo o numero de vezes que a palavra aparece'''
    i=str.split(frases)
    dicio={}
    y=1
    for x in range(0,len(i)):
        if i[x] not in dicio:
            dicio[i[x]]=(list.count(i,i[x])) 
    return dicio