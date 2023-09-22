def retira_pontuacao(frase):
    """funcao que dado de entrada uma frase, retorna a 
    propria frase onde todos os caracteres de pontuacao
    sao substituidos por espaço;
    str -> str"""
    
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'!',' '),'?',' ')