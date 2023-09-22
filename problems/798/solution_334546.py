def freq_palavras(frases):
    '''Função que retorna um dicionário, sendo suas chaves
    as palavras da string e seus valores a quantidade de vezes
    que as palavras aparecem na frase; recebe uma frase dada
    pelo usuário; String-->Dict.'''
    dicionario={}
    lista_frase= str.split(frases)
    for palavra in frases:
        dicionario[palavra]=list.count(frases,palavra)
    return dicionario