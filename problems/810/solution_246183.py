def retira_pontuacao(frase):
    """ dado uma frase, retorna a frase com a pontuacao
    substituida por espaco
    str -> str"""
    trav = str.replace(frase,'-',' ')
    virgula = str.replace(trav,',',' ')
    dois_pontos = str.replace(virgula,':',' ')
    ponto_virgula = str.replace(dois_pontos,';',' ')
    ponto = str.replace(ponto_virgula,'.',' ')
    exclam = str.replace(ponto,'!',' ')
    inter = str.replace(exclam,'?',' ')
    return inter



def inverte(frase):
    """ dado uma frase, retorna outra frase que possui
    as mesmas palavras da frase de entrada porem na ordem 
    inversa sem letras maiusculas e sem pontuacao
    str -> str"""
    sem_pontuacao = retira_pontuacao(frase)
    minusculo = sem_pontuacao.lower()
    return str.split(minusculo)