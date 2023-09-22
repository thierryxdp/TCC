def retira_pontuacao(f):
    """Função retorna uma frase (f) com todos os caracteres de pontuação retirados"""
    ponto=str.replace(f,".","")
    virgula=str.replace(ponto,",",)
    travessao=str.replace(virgula,"-","")
    doispontos=str.replace(travessao,":","")
    pontovirgula=str.replace(doispontos,";","")
    exclamacao=str.replace(pontovirgula,"!","")
    interrogacao=str.replace(exclamacao,"?","")
    final=interrogacao
    return final