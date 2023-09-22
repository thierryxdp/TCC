def retira_pontuacao(frase):
    """Funcao que, dada uma frase, retorna a frase com todos os caracteres de pontuacao substituidos por espaco;
    Entrada: str
    Saida: str"""

    editada = str.replace(frase,'.',' ')
    editada = str.replace(editada,',',' ')
    editada = str.replace(editada,'-',' ')
    editada = str.replace(editada,':',' ')
    editada = str.replace(editada,';',' ')
    editada = str.replace(editada,'!',' ')
    editada = str.replace(editada,'?',' ')


    return editada