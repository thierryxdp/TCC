def conta_frases(frase):
    '''Recebe um texto e retorna a quantidade de frases contidas no texto,
    sendo que cada frase é terminada por um ponto final,
    um ponto de exclamaçao ou interrogaçao;
    str -> int'''
    x=str.split(frase,'.')
    y=str.split(str.join(x,' '),'!')
    z=str.split(str.join(y,' '),'?')
    
    return len(z)