def inverte(frase_):
    """Retorna uma frase nova que contém as mesmas
       palavras da frase de entrada mas na ordem inversa,
       sem maiúsculas e sem pontuação;str->str"""
    ponto=str.replace(frase_,'.',' ')
    exclamacao=str.replace(ponto,'!',' ')
    travessao=str.replace(exclamacao,'-',' ')
    interrogacao=str.replace(travessao,'?',' ')
    pvirgula=str.replace(interrogacao,';',' ')
    doispontos=str.replace(pvirgula,':',' ')
    virgula=str.replace(doispontos,',',' ')
    caixabaixa=str.lower(virgula)
    s=caixabaixa
    split=str.split(s,' ')
    juntar=str.join('',split)
    return juntar[-1:0:-1]