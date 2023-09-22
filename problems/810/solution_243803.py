def retira_pontuacao(frase):
    '''Ao receber uma frase, substitui todas as pontuações
    por espaço
    str -> str'''
    #substituindo as pontuações por espaço
    travessao = str.replace(frase,'-',' ')
    virgula = str.replace(travessao,',',' ')
    dois_pontos = str.replace(virgula,':',' ')
    ponto_virgula = str.replace(dois_pontos,';',' ')
    exclamacao = str.replace(ponto_virgula,'!',' ')
    interrogacao = str.replace(exclamacao,'?',' ')
    ponto = str.replace(interrogacao,'.',' ')
    return ponto

def inverte(frase):
    '''Ao receber uma frase, retorna outra com as palavras em
    ordem inversa e sem pontuação
    str -> str'''
    despontuada = retira_pontuacao(frase)
    sem_maiuscula = str.lower(despontuada[:-1])
    palavras = str.split(str.strip(sem_maiuscula,' '),' ')
    invertida = str.join(' ',palavras[::-1])
    return invertida