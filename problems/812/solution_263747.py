def retira_pontuacao(frase):
    '''
    Recebe uma string frase e retorna a frase com espaço no lugar de qualquer pontuação
    
    str -> str
    '''
    frase_sem_final=str.replace(str.replace(str.replace(frase,'?',' '),'!',' '),'.',' ')
    frase_sem_pont=str.replace(str.replace(str.replace(str.replace(frase_sem_final,'-',' '),',',' '),':',' '),';',' ')
    return frase_sem_pont