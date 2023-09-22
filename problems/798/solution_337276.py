def freq_palavras(frase):
    '''Função que recebe uma string e retorna um dicionário onde cada
palavra da string seja uma chave e tenha como valor o número de vezes
que ela aparece;
    str -> dict'''
    lista=str.split(frase)
    dicionario={}
    for elemento in range(len(lista)):
        dicionario[lista[elemento]]=list.count(lista,lista[elemento])
    return dicionario