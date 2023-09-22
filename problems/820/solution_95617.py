def posLetra(string,letra,numero):
    '''funçao que dada uma string  uma letra e um numero 
    retorna qual a posiçao que a letra aparece na string'''
    contador = 0
    ocorrencia = 0
    while contador < len(string):
        if string[contador] == letra:
            ocorrencia+=1
        contador +=1
        if ocorrencia >= numero:
            return string.find(letra)
        if ocorrencia < numero:
            return -1