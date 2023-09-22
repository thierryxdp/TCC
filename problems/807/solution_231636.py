def conta_palavras(frase):
    p = frase.split('.')
    i = str(p).split('?')
    e = str(i).split('!')
    dp = str(e).split(':')
    return len(dp), i ,p