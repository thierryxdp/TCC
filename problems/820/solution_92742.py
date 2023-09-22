def posLetra(frase,letra,x):
    '''Recebe uma string 'frase', uma letra e um número 'x';
retorna a posição da ocorrência 'x' da letra 'letra' na frase 'string';
caso não haja tantas ocorrências quanto 'x', retorna -1;
str, str, int => int'''
    i = 0
    lista = []
    if str.count(frase,'letra')<x:
        return -1
    else:
        while len(lista) < x:
            if frase[i] == letra:
                lista = lista + [frase[i]]
            i = i+1
    return i