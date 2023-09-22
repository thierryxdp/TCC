def freq_palavras(frase):
    '''função que receba uma string e retorne um dicionário onde cada palavra dessa string seja uma chave 
    e tenha como valor o número de vezes que a palavra aparece
    str-->dict'''
    dicionario={}
    novo=dict.copy(dicionario)
    palavra=str.split(frase)
    for i in palavra:
        qtd=list.count(palavra,i)
        novo[i]=qtd
    return novo