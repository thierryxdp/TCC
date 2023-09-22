def retira_pontuacao(texto):
    '''Funcao que substitui caracteres de pontuacao por espaco
    Str -> Str'''
    texto=texto.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ")
    return texto