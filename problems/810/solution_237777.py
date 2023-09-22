def sem_pontuacao(frase):
    """Função do exercício anterior já explicada"""
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"..."," ")
    frase = str.replace(frase,"."," ")
    return frase

def inverte(frase):
    """Função que dada uma frase retorna essa mesma frase na ordem inversa,
       sem letras maiúsculas, e sem a pontuação.
       str->str
       
       Parâmetros:
       frase: É a frase que será invertida e retornada sem letras maiúsculas 
              e sem pontuação
       
       returns: A frase já invertida e sem letras maiúsculas e pontuação.
    """
    return str.lower(sem_pontuacao(str.split(frase)," ")[::-1])