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
    texto = texto.replace("?"," ")
    texto = texto.replace("!"," ")
    return texto

def inverte (frase):
    '''
    A função retorna uma frase
    invertida e sem pontuação.
    string -> string
    '''
    lista = str.split(retira_pontuacao(frase),"")
    list.reverse(lista)
    return str.join("",lista)