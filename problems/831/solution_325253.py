def lingua_p(palavra):
    '''dada uma palavra em português, retorna sua tradução para a língua
    do P;
    str -> str'''
    x = str.lower(palavra)
    traducao = ''
    for letra in x:
        if letra in 'aáeéiíoóuú':
            traducao += letra + 'p' + letra
        else:
            traducao += letra
    return traducao