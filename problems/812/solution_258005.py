def retira_pontuacao(frase):
    """Função que recebe uma frase e troca todos seus caracteres de pontuaçao por espaço.
    parametros: str->str"""
    troca1 = str.replace(frase,'-',' ')
    troca2 = str.replace(troca1,',',' ')
    troca3 = str.replace(troca2,':',' ')
    troca4 = str.replace(troca3,';',' ')
    troca5 = str.replace(troca4,'?',' ')
    troca6 = str.replace(troca5,'!',' ')
    troca7 = str.replace(troca6,'.',' ')
    return troca7