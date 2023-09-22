def posLetra(string, letra, num):
    '''retorna posição da ocorrência num na string da letra escolhida. Caso não exista , retorna -1:
    str, str,int --> int'''
    ista = []
    i=0
    for pos,char in enumerate(string):
        if(char == letra):
            lista.append(pos)
            while i < num:
                i = i+1
            return lista[i]