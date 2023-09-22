def uppCons(frase):
    nova_frase = ''
    for letra in frase:
        if letra not in 'aeiouAEIOUãõâêáéí':
            nova_frase += letra.upper()
        else:
            nova_frase += letra
    return nova_frase