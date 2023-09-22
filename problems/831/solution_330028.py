def lingua_p(palavra):
    '''Dada uma palavra em português, retorna esta mesma
    palavra traduzida para a língua do P, ou seja, após cada
    vogal são inseridas as letras p e a vogal original.
    str -> str'''
    palavra.lower()
    lista_palavra = list(palavra)
    for elemento in lista_palavra:
        if elemento in 'a':
            lista_palavra[elemento]='apa'