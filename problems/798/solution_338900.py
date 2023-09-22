def freq_palavras(frases):
    '''Dada uma string, a função retorna um dicionário
    onde cada palavra é uma chave que tem como valor o 
    número de vezes que a palavra aparece na string.
    string -> dicionario'''
    
    L = list(frase)
    ocorrencia = list.count(L,palavra)
    
    for palavra in L:
        D = {palavra:ocorrencia}
    
    return D