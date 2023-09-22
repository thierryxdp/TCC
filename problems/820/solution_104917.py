def posLetra(string, letra, numero):
    ''' função que retorna a posição de letra ( indicada no parâmetro de entrada)
dada a string a qual ela se localiza, a própria letra e o número de sua ocorrência'''
    a=0
    lista = []
    while a< len(string):
        if string[a] == letra:
            lista += [a]
        a+=1
    if numero > len(lista):
        return -1
    else:
        return lista[numero-1]