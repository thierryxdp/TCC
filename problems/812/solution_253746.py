def retira_pontuacao(frase):
    """Pede uma frase e retorna a mesma frase com todos
    os caracteres de pontuação (vírgula, travessão etc.)
    substituídos por espaço.
    str->str"""
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    return frase