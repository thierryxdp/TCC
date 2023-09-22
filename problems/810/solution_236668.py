def inverte(frase):
    '''Dada uma frase, retorna essa frase com as palavras em ordem inversa, sem letras maiúsculas e sem pontuação'''
    '''String->String'''
    ponto=str.replace(frase,'.',' ')
    exclamacao=str.replace(ponto,'!',' ')
    travessao=str.replace(exclamacao,'-',' ')
    virgula=str.replace(travessao,',',' ')
    doispontos=str.replace(virgula,':',' ')
    interrogacao=str.replace(doispontos,'?',' ')
    a=str.lower(retira_pontuacao(frase))
    b=str.split(a)[::-1]
    c=str.join(' ',b)
    return c