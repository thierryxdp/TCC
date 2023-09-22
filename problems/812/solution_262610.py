def retira_pontuacao(texto):
    """Retira a pontuação de um texto e a substitui por um espaço; str -> str"""
    pontuacao=['-',',',':',';','.','!','?','...']
    frase=str.replace(texto,'-',' ')
    frase2 = str.replace(frase, ',', ' ')
    frase3 = str.replace(frase2, ':', ' ')
    frase4 = str.replace(frase3, ';', ' ')
    frase5 = str.replace(frase4, '.', ' ')
    frase6 = str.replace(frase5, '!', ' ')
    frase7 = str.replace(frase6, '?', ' ')
    frase8 = str.replace(frase7, '...', ' ')
    return frase8