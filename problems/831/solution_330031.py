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
        elif elemento in 'á':
            lista_palavra[indice]='ápá'
        elif elemento in 'â':
            lista_palavra[indice]='âpâ'
        elif elemento in 'ã':
            lista_palavra[indice]='ãpã'
        elif elemento in 'à':
            lista_palavra[indice]='àpà'
        elif elemento in 'e':
            lista_palavra[indice]='epe'
        elif elemento in 'é':
            lista_palavra[indice]='épé'
        elif elemento in 'ê':
            lista_palavra[indice]='êpê'
        elif elemento in 'i':
            lista_palavra[indice]='ipi'
        elif elemento in 'í':
            lista_palavra[indice]='ípí'
        elif elemento in 'o':
            lista_palavra[indice]='opo'
        elif elemento in 'ó':
            lista_palavra[indice]='ópó'
        elif elemento in 'ô':
            lista_palavra[indice]='ôpô'
        elif elemento in 'õ':
            lista_palavra[indice]='õpõ'
        elif elemento in 'u':
            lista_palavra[indice]='upu'
        elif elemento in 'ú':
            lista_palavra[indice]='úpú'
        elif elemento in 'ü':
            lista_palavra[indice]='üpü'
        else:
            lista_palavra = lista_palavra
        indice = indice + 1
    resposta = ''.join(lista_palavra)
    return resposta