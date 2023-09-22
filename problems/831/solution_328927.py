def lingua_p(palavra):
    '''função que adiciona a letra p sempre após uma vogal.'
    sempre repetindo após o p a vogal anterior.
    Exemplo: 'eu'-> epeupu
    str->str'''
    palavra_comP='' 
    vogais='AEIOUaeiouáéíóú'
    for letra in palavra:
        if letra in vogais:
            palavra_comP=palavra_comP+letra+'p'+letra
        else:
            palavra_comP=palavra_comP+letra
    return str.lower(palavra_comP)