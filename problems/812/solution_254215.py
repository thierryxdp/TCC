def retira_pontuacao(x):
    """ funcao ira substituir todos os caracteres de pontuacao por espaço
    entrada string
    saida: string"""
    x = str.replace (x,"-", " ")
    x = str.replace (x,","," ")
    x = str.replace (x,":", " ")
    x = str.replace (x,";"," ")
    x = str.replace (x,"!"," ")
    x = str.replace (x,"."," ")
    x = str.replace (x,"?"," ")
    x = str.replace (x,"..."," ")
    return x