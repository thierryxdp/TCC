def lingua_p(palavra):
    '''função que recebe uma palavra em português e traduz para a lingua do p.
    str -> str
    Explicação: a lingua do p consiste em adicionar o p''' 
    letras=''
    for letra in palavra:
        if letra in 'AEIOUaeiouáéóúí':
            letra=letra+'p'+letra
        letras=letras+letra
    return str.lower(letras)