def retira_pontuacao(frase):
    """dada uma frase, a função retorna a mesma frase com todos os caractere de pontuação
    substituídos por espaço;
    str->str"""
    frase=str.replace(',',' ')
    frase=str.replace('.',' ')
    frase=str.replace(':',' ')
    frase=str.replace(';',' ')
    frase=str.replace('-',' ')
    return frase