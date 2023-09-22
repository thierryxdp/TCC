def posLetra (string, letra, numero):
    '''Dada uma string, letra e um número indicando a 
    ocorrência, retorne em que posição da frase a ocorrência
    da letra se encontra, caso menos ocorrências que a desejada,
    a função retorna  - 1;
    str, str, int -> int'''
    if string.count(letra) < numero:
        return -1
    for aux in string:
        if aux == letra:
            count = count +1
            if count == numero:
                return pos
            pos + = 1
        return pos