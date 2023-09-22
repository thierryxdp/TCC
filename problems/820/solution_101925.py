def posLetra (string, letra, numero):
    '''Dada uma string, letra e um número indicando a 
    ocorrência, retorne em que posição da frase a ocorrência
    da letra se encontra, caso menos ocorrências que a desejada,
    a função retorna  - 1;
    str, str, int -> int'''
    if string.count (letra) < numero:
        return - 1
    else: 
        i = 0
        caract = list(string)
        while i < len(caract) and len(letra) < numero:
            if letra == caract[i]:
                list.append(letra, caract[i])
                i = i + 1
        return i - 1