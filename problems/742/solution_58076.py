def substitui(s,x,i):
#essa função substitui uma string inserida e troca a letra dentro da casa escolhida
    listaString = list(s)
    listaString[i] = x
    listaString = ''.join(listaString)
    return listaString