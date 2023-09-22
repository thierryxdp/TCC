# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    Recebe uma variável s com x caracteres.
    Calcula o valor da metade do tamanho da string (m)
    Recebe os valores do começo ao meio (c).
    Recebe os valores do meio ao fim (f).
    Guarda o simbolo "#" que se quer colocar (s) 
    Retorna a concatenação s + c + s + f + s
    str -> srt
    '''
    m = len(s)//2
    c = s[0:m]
    f = s[m:len(s)]
    s = "#"
    return s+c+s+f+s