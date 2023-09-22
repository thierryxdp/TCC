def uppCons(frase):
    s=''
    for caractere in frase:
        if caractere in 'bcçdfghjklmnpqrstvxwyz':
            s+=caractere.upper()
        else:
            s+=caractere
    return s