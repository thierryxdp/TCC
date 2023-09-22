def retira_pontuacao(frase):
    '''
    Recebe uma string frase e retorna a frase com espaço no lugar de qualquer pontuação
    
    str -> str
    '''
    frase_sem_final=str.replace(str.replace(str.replace(frase,'?',' '),'!',' '),'.',' ')
    frase_sem_pont=str.replace(str.replace(str.replace(str.replace(frase_sem_final,'-',' '),',',' '),':',' '),';',' ')
    return frase_sem_pont

def inverte(frase):
    '''
    Recebe uma string frase e retorna a frase com as palavras na ordem inversa,
    sem pontuação nem letra maiúscula
    
    str -> str
    '''
    frase_min=str.lower(retira_pontuacao(frase))
    palavras=str.split(frase_min)
    palavras_inv=list.reverse(palavras)
    frase_inv=str.join(' ',palavras_inv)
    return frase_inv