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

def inverte(frase):
    """Função que dada uma frase retorna outra contendo as mesmas palavras
    de entrada na ordem inversa,s/ letras maiúsculas e s/ pontuação;
    str -> str"""
    minusc = str.lower(frase)
    sempont = retira_pontuacao(minusc)
    listafrase = str.split(sempont)
    listainvertida = listafrase[::-1]
    str.join(' ',listafrase)
    return listafrase