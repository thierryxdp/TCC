def inverte(string):
    '''funçao que inverte uma frase e retira a pontuação e letras maiusculas.string->string'''.
    lista=str.split(retira_pontuacao(string)," ")
    list.reverse(lista)
    return str.join(" ",lista)