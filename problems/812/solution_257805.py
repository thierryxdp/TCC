def retira_pontuacao(frase):
    """função que recebe uma frase e retorna a mesma sem os
       caracteres de pontuação, que são substituídos por espaço
       str -> str"""
    frase_trav = frase.replace('-',' ')
    frase_virg = frase_trav.replace (',',' ')
    frase_2pont = frase_virg.replace(':',' ')
    frase_pont_virg = frase_2pont.replace(';',' ')
    frase_pont_final = frase_pont_virg.replace('.',' ')
    
    return frase_pont_final