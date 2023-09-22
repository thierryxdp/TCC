def posLetra(string,letra,numero):
    '''funçao que dada uma string  uma letra e um numero 
    retorna qual a posiçao que a letra aparece na string'''
    contador = 0
    ocorrencias = 0
    while contador < len(string):
        if string[contador] == letra:
            ocorrencias+=1
        if ocorrencias == numero:
            return contador
        contador +=1
    if ocorrencias < numero:
        return -1