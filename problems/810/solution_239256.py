def inverte(frase):
    """Funcao que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.
    string -> string"""
    filtro1 = str.replace(frase,'-',' ')
    filtro2 = str.replace(filtro1,',',' ')
    filtro3 = str.replace(filtro2,':',' ')
    filtro4 = str.replace(filtro3,';',' ')
    filtro5 = str.replace(filtro4,'.',' ')
    filtro6 = str.replace(filtro5,'!',' ')
    filtro7 = str.replace(filtro6,'?',' ')
    
    return filtro7