def retira_pontuacao(frase):
    """Função que recebe uma frase e retorna a frase com seus caracteres de pontuação substituídos por espaço;str->str"""
    frase1=str.replace(frase,'-',' ',)
    frase2=str.replace(frase1,',',' ',)
    frase3=str.replace(frase2,':',' ',)
    frase4=str.replace(frase3,';',' ',)
    frase5=str.replace(frase4,'...',' ',)
    frase6=str.replace(frase5,'.',' ',)
    frase7=str.replace(frase6,'!',' ',)
    frase8=str.replace(frase7,'?',' ',)
    return frase8