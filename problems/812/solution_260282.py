def retira_pontuacao(texto):
    '''Funcao que, dado um segmento de texto, retorna um outro em que todos os caracteres de pontuacao sao substituidos por espaco. Str -> str'''
    passo1 = str.count(texto, ',')
    passo2 = str.count(texto, '-')
    passo3 = str.count(texto, ';')
    passo4 = str.count(texto, ':')
    passo5 = str.count(texto, '?')
    passo6 = str.count(texto, '!')
    passo7 = str.count(texto, '.')
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
    String7 = str.replace(String6, Sete, ' ', passo7)
    return String7