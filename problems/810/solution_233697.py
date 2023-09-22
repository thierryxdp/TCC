def retira_pontuacao(frase):
    '''Substitui onde estão os caracteres de pontuação (travessão, vírgula, dois pontos , ponto e vírgula e encerramento de frase) por espaços
    string -> int'''
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,"."," ")
    frase=str.replace(frase,"?"," ")
    frase=str.replace(frase,"!"," ")
    return frase

def inverte(frase):
    """Entrega a frase na ordem inversa, sem letras maiusculas e sem pontuação
    string -> string"""
    frase = str.lower(frase)
    frase = retira_pontuacao(frase)
    frase = str.split(frase," ")
    frase = frase[-1:]
    #frase = str.join(frase," ")
    return frase