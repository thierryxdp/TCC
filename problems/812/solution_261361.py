def retira_pontuacao(texto):
    ''' Função que subistitui todos os caracteres de pontuação por espaço
    String-> String'''
    texto = str.replace(texto, "-"," ")
    texto = str.replace(texto, ","," ")
    texto = str.replace(texto, ":"," ")
    texto = str.replace(texto, ";"," ")
    texto = str.replace(texto, "."," ")
    texto = str.replace(texto, "?"," ")
    texto = str.replace(texto, "!"," ")
    texto = str.replace(texto, "..."," ")
    
    return texto