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