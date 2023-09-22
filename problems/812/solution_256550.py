def retira_pontuacao(frase):
    '''Dada uma frase, retorna a mesma frase com todos os caracteres de pontuação substituídos por espaço'''
    '''string->string'''
    ponto=str.replace(frase,'.',' ')
    exclamacao=str.replace(ponto,'!',' ')
    travessao=str.replace(exclamacao,'-',' ')
    virgula=str.replace(travessao,',',' ')
    doispontos=str.replace(virgula,':',' ')
    interrogacao=str.replace(doispontos,'?',' ')
    return interrogacao