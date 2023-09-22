def retira_pontuacao(string):
    '''função que retira a pontuação de uma string e substitui por espaço. string -> string.'''
    string = string.replace(","," ")
    string = string.replace("!"," ")
    string = string.replace("?"," ")
    string = string.replace(":"," ")
    string = string.replace(";"," ")
    string = string.replace("."," ")
    string = string.replace("_"," ")
    return string
    return string
def inverte (string):
    lista = str.split(retira_pontuacao(string)," ")
    list.reverse (lista)
    return str.join(" ", lista )