def inverter(frase):
    '''
    funcao que dada uma frase em string retorna uma frase
    com as mesmas palavras da frase de entrada, mas em
    ordem inversa, sem pontuacao e sem letras maiusculas
    string->string
    '''
    travessao=frase.replace('-',' ')
    virgula=travessao.replace(',',' ')
    doisPontos=virgula.replace(':',' ')
    pontoEvirgula=doisPontos.replace(';',' ')
    ponto=pontoEvirgula.replace('.',' ')
    exclamacao=ponto.replace('!',' ')
    interrogacao=exclamacao.replace('?',' ')
    reticencias=interrogacao.replace('...',' ')
    frasefinal=reticencias
    minusculas=str.lower(frasefinal)
    palavras=str.split(minusculas)
    invertida=list.reverse(palavras)
    return str.join(' ',palavras)