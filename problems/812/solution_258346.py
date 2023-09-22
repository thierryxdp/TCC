def retira_pontuacao(frase):
    '''Funcao que calcula e retorna a retirada de pontuacao e substitui por espaço'''
    o1 = str.replace(frase,"-"," ")
    o2 = str.replace(o1,","," ")
    o3 = str.replace(o2,":"," ")
    o4 = str.replace(o3,";"," ")
    o5 = str.replace(o4,"."," ")
    o6 = str.replace(o5,"!"," ")
    o7 = str.replace(o6,"?"," ")
    return o7