def posLetra(texto,l,n):
    '''função que recebe um texto, um número e uma ocorrencia e,
    retorna uma string onde a ocorrencia da letra esta.
    string, string, int ->string'''
    lista = list(texto)
    cont = texto.count(l)
    
    if cont>=n:
        substitui = str.replace(texto,l,'&',n-1)
        return str.find(substitui,l,0,-1)
    else:
        return -1