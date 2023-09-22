def retira_pontuacao(frase):
    '''recebe uma frase com pontuações e retorna uma nova frase onde todas as pontuações foram substituídas por espaço.
    str -> str'''
    return str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'.',' ')