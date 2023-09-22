def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a frase onde todos os caracteres
    de pontuação (incluindo travessão, vírgula, dois pontos, ponto e vírgula,
    além da pont. de encerramento de frase) tenham sido substituídos por
    espaço;
    str -> str"""
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    doisPontos = virgula.replace(':', ' ')
    pontoVirgula = doisPontos.replace(';', ' ')
    pontoFinal = pontoVirgula.replace('.', ' ')
    pontoInterrog = pontoFinal.replace('?', ' ')
    pontoExclam = pontoInterrog.replace('!', ' ')
    return pontoExclam
#Remova a pontuação da frase, usando a função anterior
def inverte(frase):
    """Função que dada uma frase retorna outra contendo as mesmas palavras
    da frase de entrada na ordem inversa, s/ letras maiúsculas, e s/ pontuação;
    str -> str
    """
    sempont = retira_pontuacao(frase)
    minusc = str.lower(frase)
    listafrase = str.split(sempont)
    listainvertida = listafrase[::-1]
    str.join(' ',listainvertida)
    return listainvertida