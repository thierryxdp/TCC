def lingua_p(palavra):
    '''Dada uma palavra em portugues, retorna essta mesma
palavra traduzida para a lingua do p. str -> str'''
    nova=''
    V='aeiou'
    for letra in palavra:
        if str.lower(letra) in V:
            s+=str.lower(letra)+p+V[str.find(V,str.lower(letra))]
        else:
            s+=str.lower(letra)
    return s