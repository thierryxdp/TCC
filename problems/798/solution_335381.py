def freq_palavras(frase):
    '''funcao que recebe uma string e retorna um dicionario no qual cada palavra seja uma chave e os valores representam o numero de vezes que a palavra aparece
    str -> dict'''
    dicionario_saida={}
    lista=str.split(frase)
    for i in lista:
        dicionario_saida=dicionario_saida+{i:str.count(frase,i),}
    return dicionario_saida