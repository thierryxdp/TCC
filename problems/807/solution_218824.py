def conta_frases(frase):
    '''Recebe um texto e retorna a quantidade de frases contidas no texto,
    sendo que cada frase é terminada por um ponto final,
    um ponto de exclamaçao ou interrogaçao;
    str -> int'''
    x=str.join('/',(str.split(frase,'...')))
    y=str.join('/',(str.split(x,'?')))
    z=str.join('/',(str.split(y,'!')))
    w=str.join('/',(str.split(z,'.')))
    q= str.split(w,'/')
    
    return len(q)-1