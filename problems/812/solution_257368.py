def retira_pontuacao(frase):
    """Recebe uma frase e retorna a mesma frase, mmas sem os caracteres de pontuação
       parâmetros de entrada:str
       parâmetros de saída:str"""
    frase=str.replace(frase,'--',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'.',' ')
    return frase