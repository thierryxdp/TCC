def freq_palavras(frases):
    '''
    funcao que recebe uma string e retorna um
    dicionario em que cada palavra da string
    é uma chave e seu valor a quantidade de
    vezes que ela aparece na string
    string->dict
    '''
    dic={}
    x=str.split(frases)
    for y in x:
        if y in dic:
            dic[y]=dic[y]+1
        else:
            dic[y]=1
    return dic