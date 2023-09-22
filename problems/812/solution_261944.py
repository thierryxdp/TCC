def retira_pontuacao(texto):
    lista = str.replace(texto, "-", "")
    lista = str.replace(lista, ",", "")
    lista = str.replace(lista, ":", "")
    lista = str.replace(lista, ";", "")
    lista = str.replace(lista, ".", "")
    
    return (lista)