def retira_pontuacao(frase):
    '''A partir da frase de entrada retira a pontuacao, torna todas as 
    letras minusculas e escreve as palavras na ordem inversa da original
    str -> str'''
    ponto = str.replace(frase,'.',' ')
    virgula = str.replace(ponto,',',' ')
    doispontos = str.replace(virgula,':',' ')
    pontovirgula = str.replace(doispontos,';',' ')
    travessao = str.replace(pontovirgula,'—',' ')
    interrogacao = str.replace(travessao,'?',' ')
    exclamacao = str.replace(interrogacao,'!',' ')
    hifen = str.replace(exclamacao,'-',' ')
    minuscula = str.lower(hifen)
    listafrase = str.split(minuscula)
    listafraseinversa = listafrase[-1:0:-1]
    return str.join(' ',listafraseinversa)