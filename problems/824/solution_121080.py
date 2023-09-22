def uppCons(texto):
    cont=0
    texto.lower()
    texto_cons=[]
    while cont<len(texto):
        if texto[cont]in 'BCÇDFGHJKLMNPQRSTVXWYZ':
            texto_nova=texto_nova + [texto[cont]]
        else:
            texto_nova=texto_nova + [texto[cont]]
        cont=cont+1
        texto_nova="".join(texto_nova)
    return texto