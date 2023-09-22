def retira_pontuacao(texto):
    lista = str.replace(texto, "-", "")
    lista = str.replace(texto, ",", "")
    lista = str.replace(texto, ":", "")
    lista = str.replace(texto, ";", "")
    lista = str.replace(texto, ".", "")
    
    return (lista)