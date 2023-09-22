def retira_pontuacao(frase):
    
    a = str.join(' ', str.split(frase, '.'))
    b = str.join(' ', str.split(frase, ','))
    c = str.join(' ', str.split(frase, '?'))
    d = str.join(' ', str.split(frase, '!'))
    e = str.join(' ', str.split(frase, '-'))
    return e