def retira_pontuacao(frase):
    '''retorna a frase fornecida com os caracteres de pontuacao
    substituidos por espacos; str -> str'''
    
    return ((((frase.replace(',',' ')).replace('.',' ')).replace('!',' ')).replace('-',' ')).replace('?',' ')