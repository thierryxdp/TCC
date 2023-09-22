def  uppCons(texto):
    ''' função que recebe uma frase e devolve as consoantes
    em caixa alta (letra maiúscula)'''
    'str----->str'
    
    lista_texto = list(texto)
    i = 0
    letras = []

    while  i  <  len(lista_texto):
        if  lista_texto[i]  in  'cçbcdfghjklmnpqrstvwxyz':
            letras.insert(i, lista_texto[i].upper())
            i = i + 1
        else:
            letras.insert(i, lista_texto[i])
            i = i + 1

    return  ''.join(letras)