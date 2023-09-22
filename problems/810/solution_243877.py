def retira_pontuacao(frase):
    """Função que recebe uma frase e retorna uma frase onde todos os
    caracteres de pontuação tenham sido substituídos por espaços.
    str->str
    """
    frase = str.replace(frase, "-", " " )
    frase = str.replace(frase, ",", " " )
    frase = str.replace(frase, ":", " " )
    frase = str.replace(frase, ";", " " )
    frase = str.replace(frase, "?", " " )
    frase = str.replace(frase, "!", " " )
    frase = str.replace(frase, ".", " " )
    frase = str.replace(frase, "...", " " )
    return frase

def inverte(frase):
    """Função que recebe uma frase e retorna outra frase que contenha
    as mesmas palavras da frase original, mas na ordem inversa, sem
    letra maiúscula e sem pontuação.
    str->str
    """
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    frase = str.split(frase)
    frase = list(frase)
    list.reverse(frase)    
    frase = str.join(' ', frase)
    return frase