def retira_pontuacao (frase):
    """funçao que recebe uma frase e substitui toda sua pontuaçao por espaço
entrada: str;
saida: str."""
    if (frase in '.'):
        frase = str.replace (frase, '.', ' ')

    if (frase in '!'):
        frase = str.replace (frase, '!', ' ')

    if (frase in '?'):
        frase = str.replace (frase, '?', ' ')

    if (frase in '...'):
        frase = str.replace (frase, '...', ' ')

    if (frase in '-'):
        frase = str.replace (frase, '-', ' ')

    if (frase in ','):
        frase = str.replace (frase, ',', ' ')

    if (frase in '-'):
        frase = str.replace (frase, ':', ' ')

    if (frase in '-'):
        frase = str.replace (frase, ';', ' ')
    return frase