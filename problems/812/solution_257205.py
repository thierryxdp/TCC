def retira_pontuacao(frase):
    '''dada uma frase, retorna a frase onde todos os caracteres de pontuação foram substituídos por espaço'''
    a = str.replace(frase,"."," ")
    b = str.replace(a,"..."," ")
    c = str.replace(b,"!"," ")
    d = str.replace(c,";"," ")
    e = str.replace(d,":"," ")
    f = str.replace(e,"?"," ")
    g = str.replace(f,","," ")
    h = str.replace(g,"-"," ")
    return h