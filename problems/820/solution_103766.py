def posLetra(frase,letra,repeticao):
    '''retorna o índice onde uma letra se repete pela x vez. 
    caso não se repita o suficiente, retorna '-1'
    str->int'''
    i=frase.find(letra)
    while i>=0 and repeticao>1:
        if letra != frase:
            return -1
        i= frase.find(frase,i+1)
    return i