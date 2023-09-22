def retira_pontuação (frase):
    """dada uma frase, função retorna a frase onde todos os caracteres
    de pontuação são substituídos por espaço"""
    """string -> string"""
    F = frase
    F1 = str.replace(F, '-', ' ')
    F2 = str.replace(F1,',', ' ')
    F3 = str.replace(F2,':', ' ')
    F4 = str.replace(F3,';', ' ')
    F5 = str.replace(F4,'.', ' ')
    F6 = str.replace(F5,'!', ' ')
    F7 = str.replace(F6,'?', ' ')
    return F7