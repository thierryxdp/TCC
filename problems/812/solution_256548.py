def retira_pontuacao(texto):
    """Substitui qualquer sinal de um texto por vírguloas.
       string -> string"""
    texto = str.replace(texto,"-"," ")
    texto = str.replace(texto,"."," ")
    texto = str.replace(texto,","," ")
    texto = str.replace(texto,":"," ")
    texto = str.replace(texto,";"," ")
    texto = str.replace(texto,"!"," ")
    texto = str.replace(texto,"?"," ")
    return texto