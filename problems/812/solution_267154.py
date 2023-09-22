def retira_pontuacao(s):
    """recebe uma string e substitui todos os caracteres de pontuação por espaços
    str->str"""
    s=s.replace(","," ")
    s=s.replace("."," ")
    s=s.replace("-"," ")
    s=s.replace(";"," ")
    s=s.replace(":"," ")
    s=s.replace("?"," ")
    s=s.replace("!"," ")
    return s