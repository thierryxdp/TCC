def uppCons(frase):
    '''recebe uma frase e a retorna com todas as consoantes maiusculas
    str --> str'''
    fraseM = str.upper(frase)
    lista = list(fraseM)
    i = 1
    lista_final = []
    while i < len(lista):
        if lista[i] in 'AEIOUÁÉÍÓÚÃÕÂÊÎÔÛÀ':
            list.append(lista_final,lista[i])
        else: 
            list.append(lista_final,lista[i])
        i = i + 1
    consM = fraseM[0]+str.join('',lista_final)
    return consM