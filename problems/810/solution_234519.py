def inverte(f):
    """Função recebe uma frase e a retorna sem pontuação e com a ordem das palavras invertida;
    str->str"""
    ponto=str.replace(f,"."," ")
    virgula=str.replace(ponto,","," ")
    travessao=str.replace(virgula,"-"," ")
    doispontos=str.replace(travessao,":"," ")
    pontovirgula=str.replace(doispontos,";"," ")
    exclamacao=str.replace(pontovirgula,"!"," ")
    interrogacao=str.replace(exclamacao,"?"," ")
    minusculo=str.lower(interrogacao)
    final=minusculo
    novafrase=str.split(final)[len(final)::-1]
    return str.join(" ",novafrase)