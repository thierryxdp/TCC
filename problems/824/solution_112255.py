def uppCons(frase:str)->str:
    count = 0
    aux = []
    while count < len(frase):
        if frase[count] in 'bcçdfghjklmnpqrstvwxyz':
            aux.append(frase[count].upper())
        else:
            aux.append(frase[count])
        count += 1
    return ''.join(aux)