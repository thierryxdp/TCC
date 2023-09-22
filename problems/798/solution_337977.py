def freq_palavras(frases):
    '''
    função que recebe uma string e retorna um dicionário
    onde cada palavra dessa string seja uma chave e tenha 
    como valor o número de vezes que cada palavra aparece
    '''
    dicionario = { }
    palavra = str.split(frases)
    
    for elemento in palavra:
        if elemento in palavra:
            dicionario[elemento] = list.count(palavra,elemento)
    return dicionario