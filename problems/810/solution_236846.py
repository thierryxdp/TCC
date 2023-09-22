def retira_pontuacao (frase):
    """funçao que recebe uma frase e substitui toda sua pontuaçao por espaço
entrada: str;
saida: str."""
    frase = str.replace (frase, '.', ' ')
    frase = str.replace (frase, '!', ' ')
    frase = str.replace (frase, '?', ' ')  
    frase = str.replace (frase, '-', ' ')
    frase = str.replace (frase, ',', ' ')
    frase = str.replace (frase, ':', ' ')
    frase = str.replace (frase, ';', ' ')
    frase = str.replace (frase, '...', ' ')
    return frase

def inverte (frase):
    """funçao que recebe uma frase e retorna essa frase em ordem inversa, em letra minuscula e sem pontuaçao;
entrada: str;
saida: str."""
    frase = retira_pontuacao (frase)
    frase = str.split (frase, )
    frase = frase [::-1]
    frase = str.join (' ',frase)
    return str.lower (frase)