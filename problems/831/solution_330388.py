def lingua_p(palavra):
    '''Recebe uma palavra e retorna sua tradução para a
    língua do P.
    str -> str'''
    # Transformando todas as possíveis letras maiúsculas
    # em minúsculas:
    palavra = str.lower(palavra)
    # Realizando o procedimento:
    traducao = ''
    for i in palavra:
        if i in 'aeiouáéíóú':
            traducao += i+'p'+i
        else:
            traducao += i
    return traducao