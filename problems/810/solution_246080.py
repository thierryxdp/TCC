def inverte(txt):
    lista = []
    txt = frases_sem_pontuacao(txt)
    txt = txt.lower()
    lista = lista + str.split(txt)
    lista.reverse()
    x = " ".join(lista)
    return x