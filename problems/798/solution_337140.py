def freq_palavras(f):
    '''Recebe uma string e retona um dicionario onde cada palavra dessa string é uma chave e 
    tenha como valor do numero de vezes que a palavra aparece na string
    str -> dict'''
    dic={}
    f=f.strip()
    f=f.split(' ')
    for palavra in f:
        if palavra in dic:
            dicionario[palavra]=dic[palavra]+1
        else:
            dic[palavra]=1
    return dic