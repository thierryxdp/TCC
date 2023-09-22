def posLetra(frase,letra,numero):
    '''função que dada uma string, uma letra e um número que indique o número da ocorrência
       da letra, retorna a posição na qual a ocorrência desta letra se encontra. Se o número
       for maior que o número de ocorrências desta letra, retorna -1. str, str, int -> int'''
    pos = 0
    indice = 0
    while pos < len(frase):
        if (str.count(frase,letra) >= numero) and (frase[pos] == letra):
            indice = str.index(frase,letra)
        else:
            indice = -1
        pos = pos + 1
    return indice