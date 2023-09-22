def freq_palavras(frase):
    '''função que recebe uma string e retorna um dicionário
    onde cada palavra da string é uma chave seguida do 
    respectivo número de vezes que a palavra aparece'''
    dicionario={}
    for palavra in frase:
        if palavra in frase:
            count = 1
            dicionario[palavra] = palavra + ' ' + str(count)
    return dicionario