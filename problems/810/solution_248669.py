def retira_pontuacao(frase):
    
    a = str.join(' ', str.split(frase, '.'))
    b = str.join(' ', str.split(a, ','))
    c = str.join(' ', str.split(b, '?'))
    d = str.join(' ', str.split(c, '!'))
    e = str.join(' ', str.split(d, '-'))
    return e
def inverte(frase):
    lista_errada=[]
    frase_limpa=retira_pontuacao(frase)
    lista_correta=frase_limpa.split()
    lista=list.append(lista_errada,lista_correta)
    nova_frase=str.join(" ",lista)
    return nova_frase