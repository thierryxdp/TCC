def freq_palavras(frase):
    ''' Função que recebe uma string e retorna um dicionário
    onde cada palavra da string de entrada será uma chave e
    como valor terá o número de vezes que a palavra aparece
    str -> dict '''
    dicio = {}
    frase_lista = str.split(frase,' ')
    for palavra in frase_lista:
        dicio[palavra]=list.count(frase_lista,palavra)
    return dicio