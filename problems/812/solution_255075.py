def retira_pontuacao(frase):
    """Dada uma frase retorna a mesma sem pontuação string -> string"""
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"..."," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    return str.replace(frase,"."," ")