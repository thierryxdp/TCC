def retira_pontuacao (frase):
    """funçao que recebe uma frase e substitui toda sua pontuaçao por espaço
entrada: str;
saida: str."""
    if (frase in '.'):
        frase = str.replace (frase, '.', ' ')

    elif (frase in '!'):
        frase = str.replace (frase, '!', ' ')

    elif (frase in '?'):
        frase = str.replace (frase, '?', ' ')

    elif (frase in '...'):
        frase = str.replace (frase, '...', ' ')

    elif (frase in '-'):
        frase = str.replace (frase, '-', ' ')

    elif (frase in ','):
        frase = str.replace (frase, ',', ' ')

    elif (frase in '-'):
        frase = str.replace (frase, ':', ' ')

    elif (frase in '-'):
        frase = str.replace (frase, ';', ' ')
    
    else:
        return frase