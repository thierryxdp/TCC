def tirar_pontuacao(frase):
    '''Funcao que calcula e retorna a retirada de pontuacao e substitui por espaço'''
    a1=str.replace(frase,"-"," ")
    a2=str.replace(a1,","," ")
    a3=str.replace(a2,":"," ")
    a4=str.replace(a3,";"," ")
    a5=str.replace(a4,"."," ")
    a6=str.replace(a5,"!"," ")
    a7=str.replace(a6,"?"," ")
    return a7