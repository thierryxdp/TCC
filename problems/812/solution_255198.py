def retira_pontuacao (texto):
    '''
    A função que retorna o texto
    sem a pontuação.
    string -> string
    '''
    texto = texto.replace(","," ")
    texto = texto.replace("."," ")
    texto = texto.replace("-"," ")
    texto = texto.replace(";"," ")
    texto = texto.replace(":"," ")
    texto = texto.replace("!"," ")
    texto = texto.replace("?"," ")
    return texto