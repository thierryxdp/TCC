def retira_pontuacao(texto):
    '''Funcao que, dado um segmento de texto, retorna um outro em que todos os caracteres de pontuacao sao substituidos por espaco. Str -> str'''
    texto_copia = texto[:]
    passo1 = str.count(texto_copia, ',')
    passo2 = str.count(texto_copia, '-')
    passo3 = str.count(texto_copia, ';')
    passo4 = str.count(texto_copia, ':')
    passo5 = str.count(texto_copia, '?')
    passo6 = str.count(texto_copia, '!')
    passo7 = str.count(texto_copia, '.')
    Um = ','
    Dois = '-'
    Tres = ';'
    Quatro = ':'
    Cinco = '?'
    Seis = '!'
    Sete = '.'
    String1 = str.replace(texto, Um, ' ', passo1)
    String2 = str.replace(String1, Dois, ' ', passo2)
    String3 = str.replace(String2, Tres, ' ', passo3)
    String4 = str.replace(String3, Quatro, ' ', passo4)
    String5 = str.replace(String4, Cinco, ' ', passo5)
    String6 = str.replace(String5, Seis, ' ', passo6)
    String_SemPontuacao = str.replace(String6, Sete, ' ', passo7)
    return String_SemPontuacao