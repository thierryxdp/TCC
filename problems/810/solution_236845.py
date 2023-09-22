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