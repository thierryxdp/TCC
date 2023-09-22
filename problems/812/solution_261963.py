def retira_pontuacao(texto):
    a = ()
    lista = str.replace(texto, "-"," " )
    lista = str.replace(lista, ",", " ")
    lista = str.replace(lista, ":", " ")
    lista = str.replace(lista, ";", " ")
    lista = lista[:-2] + lista[-1]
    
    return (lista)