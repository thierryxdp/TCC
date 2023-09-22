def freq_palavras(frases):
    '''funcao que recebe uma string e retorna um dicionario que retorna cada palavra dessa string
    como uma chave e tenha como valor quantas vezes a mesma aparece'''
'''str->dic'''
    div=frases.split(' ')
    dic={}
    for i in div:
        dic[i]=div.count(i)
    return dic