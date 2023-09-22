def frase_inversa(texto):
    '''Funcao que, dado um segmento de texto, o retorna com a ordem das palavras invertida. Str -> Str.'''
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
    frase_sem_ponto = str.replace(String6, Sete, ' ', passo7)
    minusculo = str.lower(frase_sem_ponto)
    palavras = str.split(minusculo)
    ordem_inversa = palavras[::-1]
    string = str.join(' ', ordem_inversa)
    return string