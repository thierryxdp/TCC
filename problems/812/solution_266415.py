def retira_pontuacao(texto):
    lista=[]
    lista[:]=texto
    a=[]
    p1=list.index(lista,'/')
    while '/' in lista:
       lista[p1]= ' '
       return lista