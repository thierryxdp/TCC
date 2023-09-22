def retira_pontuacao (frase):
    """funçao que recebe uma frase e substitui toda sua pontuaçao por espaço
entrada: str;
saida: str."""
    
    if frase in '.':
        frase = str.replace (str.rstrip (frase, '.'))
    
    return frase