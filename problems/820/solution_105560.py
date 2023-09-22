def posLetra(string, letra, num):
    '''retorna posição da ocorrência num na string da letra escolhida. Caso não exista , retorna -1:
    str, str,int --> int'''
    lista = []
    i= num - 1
    for pos,char in enumerate(string):
        if(char == letra):
            lista.append(pos)
    return lista[i]