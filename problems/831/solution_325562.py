def lingua_p(palavra):
    '''Função que dada uma palavra, retorna a mesma palavra traduzida para a língua do P e toda em minúsculas
    str -> str'''
    vogais='aeiouáéíóúêôã'
    palavra_m=str.lower(palavra)
    palavra_final=''
    for letra in palavra_m:
        if letra in vogais:
            palavra_final+=letra+'p'+letra
        else:
            palavra_final+=letra
    return palavra_final