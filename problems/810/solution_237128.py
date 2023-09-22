def inverte(frase_):
    """Retorna uma frase nova que contém as mesmas
       palavras da frase de entrada mas na ordem inversa,
       sem maiúsculas e sem pontuação;str->str"""
    frase_=str.strip(frase_)
    ponto=str.replace(frase_,'.',' ')
    exclamacao=str.replace(ponto,'!',' ')
    travessao=str.replace(exclamacao,'-',' ')
    interrogacao=str.replace(travessao,'?',' ')
    pvirgula=str.replace(interrogacao,';',' ')
    doispontos=str.replace(pvirgula,':',' ')
    virgula=str.replace(doispontos,',',' ')
    espaco=str.replace(virgula,'  ',' ')
    caixabaixa=str.lower(espaco)
    split=str.split(caixabaixa,' ')
    juntar=str.join(' ',split[-1::-1])
    return juntar