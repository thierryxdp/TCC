def retira_pontuacao(frase):
    """dada uma frase, a função retorna a mesma frase com todos os caractere de pontuação
    substituídos por espaço;
    str->str"""
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    return frase