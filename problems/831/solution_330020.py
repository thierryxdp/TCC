def lingua_p(palavra):
    '''Dada uma palavra em português, retorna esta mesma
    palavra traduzida para a língua do P, ou seja, após cada
    vogal são inseridas as letras p e a vogal original.
    str -> str'''
    palavra.lower()
    lista_palavra = list(palavra)
    for elemento in lista_palavra:
        indice = lista_palavra.index(elemento)
        if elemento == 'a':
            lista_palavra[indice:indice]=['pa']
        elif elemento == 'e':
            lista_palavra[indice:indice]=['pe']
        elif elemento == 'i':
            lista_palavra[elemento:elemento]=['pi']
        elif elemento == 'o':
            lista_palavra[elemento:elemento]=['po']
        elif elemento == 'u':
            lista_palavra[elemento:elemento]=['pu']
        else:
            lista_palavra = lista_palavra
	''.join(lista_palavra)
    return lista_palavra