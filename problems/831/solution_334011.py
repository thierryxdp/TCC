def lingua_p(palavra):
    '''Dada uma palavra em portugues, retorna essta mesma
palavra traduzida para a lingua do p. str -> str'''
    nova=''
    V='aáàâãéêeíìióôõoúu'
    for letra in palavra:
        if str.lower(letra) in V:
            nova+=str.lower(letra)+'p'+V[str.find(V,str.lower(letra))]
        else:
            nova+=str.lower(letra)
    return nova