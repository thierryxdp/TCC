def retira_pontuacao(frase):
    '''funcao que retira todas as pontuações de uma frase e as substitui por um espaço;
    str -> str'''
    frase1 = str.replace(frase,',','')
    frase2 = str.replace(frase1,'!','')
    frase3 = str.replace(frase2,'?','')
    frase4 = str.replace(frase3,'.','')
    frase5 = str.replace(frase4,'-','')
    frase6 = str.replace(frase5,';','')
    frase7 = str.replace(frase6,':'.'')
    frase8 = str.replace(frase7,'...','')
    return frase8