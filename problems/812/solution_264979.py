def retira_pontuacao(x=""):
    '''função que retira os caracteres de pontuação da frase dada
    e os substitui por espaços'''
    x=x.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ")
    return x