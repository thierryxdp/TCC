def retira_pontuacao(string):
    '''função que retira a pontuação de uma frase e substitui por espaço.string->string.'''
    string=string.replace(","," ")
    string=string.replace("!"," ")
    string=string.replace("?"," ")
    string=string.replace(":"," ")
    string=string.replace(";"," ")
    string=string.replace("."," ")
    string=string.replace("-"," ")
    return string
def inverte(string):
    '''função que dada uma frase retorna outra frase que contem as mesmas palavras da frase de entrada na ordem inversa.string->string.'''
    lista=str.split(retira_pontuacao(string)," ")
    list.reverse(lista)
    return str.join(" ",lista)