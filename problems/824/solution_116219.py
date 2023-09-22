def uppCons(frase):
    '''recebe uma frase e a retorna com todas as consoantes maiusculas
    str --> str'''
    fraseM = str.upper(frase)
    lista = list(fraseM)
    lista_final = []
    i = 1
    while i < len(lista):
        if lista[i] in 'AEIOUÁÉÍÓÚÃÕÂÊÎÔÛÀ':
            list.append(lista_final, str.lower(lista[i]))
        else: 
            list.append(lista_final,lista[i])
        i = i + 1
    consM = fraseM[0] + str.join('',lista_final)
    return consM