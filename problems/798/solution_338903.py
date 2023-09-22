def freq_palavras(frase):
    '''Dada uma string, a função retorna um dicionário
    onde cada palavra é uma chave que tem como valor o 
    número de vezes que a palavra aparece na string.
    string -> dicionario'''
    
    L = ' '.list(frase)
    
    for palavra in L:
        ocorrencia = list.count(L,palavra)
        D = {palavra:ocorrencia}
    
    return D