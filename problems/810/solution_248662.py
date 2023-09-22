def retira_pontuacao(frase):
    
    a = str.join(' ', str.split(frase, '.'))
    b = str.join(' ', str.split(a, ','))
    c = str.join(' ', str.split(b, '?'))
    d = str.join(' ', str.split(c, '!'))
    e = str.join(' ', str.split(d, '-'))
    return e
def inverte(frase):
    frase_limpa=retira_pontuacao(frase)
    lista_correta=frase_limpa.split()
    lista_errada=list.append(lista_correta[-1:])
    nova_frase=str.join(" ",lista_errada)
    return nova_frase