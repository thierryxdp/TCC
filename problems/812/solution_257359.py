def retira_pontuacao(frase):
    """Recebe uma frase e retorna a mesma frase, mmas sem os caracteres de pontuação
       parâmetros de entrada:str
       parâmetros de saída:str"""
    frase1=str.replace(frase,'--','')
    frase2=str.replace(frase,',','')
    frase3=str.replace(frase,':','')
    frase4=str.replace(frase,';','')
    frase5=str.replace(frase,'?','')
    frase6=str.replace(frase,'!','')
    return frase1+frase2+frase3+frase4+frase5+frase6