def conta_frases(frase):
    '''Recebe um texto e retorna a quantidade de frases contidas no texto,
    sendo que cada frase é terminada por um ponto final,
    um ponto de exclamaçao ou interrogaçao;
    str -> int'''
    x=str.split(frase,'.')
    y=str.split(x,'!')
    z=str.split(y,'?')
    
    return len(z)