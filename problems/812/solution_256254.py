def retira_pontuacao (frase):
    """funçao que recebe uma frase e substitui toda sua pontuaçao por espaço
entrada: str;
saida: str."""
    if (frase in '.' or '!' or '?' or '...' or '-' or ':' or ';' or ','):
        return str.replace (frase, '.' or '!' or '?' or '...' or '-' or ':' or ';' or ',', ' ')
    else:
        return frase