def retira_pontuacao(frase):
    '''
       Função que recebe uma frase e substitui todas as suas pontuações por espaço
       str --> str
    '''
    nova_frase = frase.replace('-',' ')
    nova_frase = frase.replace(',',' ')
    nova_frase = frase.replace(':',' ')
    nova_frase = frase.replace(';',' ')
    nova_frase = frase.replace('.',' ')
    
    return nova_frase