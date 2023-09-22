def posLetra(string, letra, numero):
    '''Função que dada uma string, uma letra e um número, retorna
    a posição que essa letra aparece na ocorrência desejada.
    string -> str
    letra -> str
    numero -> int'''
    ocorrencias = 0 
    i = 0
    
    while i< len(string):
        if string[i] == letra:
            ocorrencias += 1
        i+= 1
        if ocorrencias == numero:
            return i