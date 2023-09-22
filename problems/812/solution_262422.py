def retira_pont(frase):
    '''Função que troca todas as pontuações de uma frase por espaços;
    str -> str'''
    
    frase.remove('?') + frase.remove('!') + frase.remove('.') + frase.remove('-') + frase.remove(',') + frase.remove(';')
    
    return frase