def retira_pontuacao(frase):
    
    a = str.join(' ', str.split(frase, '.'))
    b = str.join(' ', str.split(a, ','))
    c = str.join(' ', str.split(b, '?'))
    d = str.join(' ', str.split(c, '!'))
    e = str.join(' ', str.split(d, '-'))
    return e
def inverte(frase):
    frase_limpa=retira_pontucao(frase)
    lista=frase_limpa.split()
    nova_frase=str.join(" ",lista)
    return nova_frase