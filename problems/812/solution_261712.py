def retira_pontuacao(frase):
    '''funcao que ao receber uma dada frase, retira todos os caracteres de pontuacao, substituindo por espaço
    string -> string'''
    frase_sem_ponto = str.replace(frase,'-',' ')
    frase_sem_ponto = str.replace(frase,'.',' ')
    frase_sem_ponto = str.replace(frase,',',' ')
    frase_sem_ponto = str.replace(frase,';',' ')
    frase_sem_ponto = str.replace(frase,':',' ')
    frase_sem_ponto = str.replace(frase,'!',' ')
    frase_sem_ponto = str.replace(frase,'?',' ')
    return frase_sem_ponto