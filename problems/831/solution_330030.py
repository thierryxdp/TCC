def lingua_p(palavra):
    '''Dada uma palavra em português, retorna esta mesma
    palavra traduzida para a língua do P, ou seja, após cada
    vogal são inseridas as letras p e a vogal original.
    str -> str'''
    palavra.lower()
    lista_palavra = list(palavra)
    indice = 0
    for elemento in lista_palavra:
        if elemento in 'a':
            lista_palavra[indice]='apa'
        elif elemento in 'e':
            lista_palavra[indice]='epe'
        elif elemento in 'i':
            lista_palavra[indice]='ipi'
        elif elemento in 'o':
            lista_palavra[indice]='opo'
        elif elemento in 'u':
            lista_palavra[indice]='upu'
        else:
            lista_palavra = lista_palavra
        indice = indice + 1
    resposta = ''.join(lista_palavra)
    return resposta