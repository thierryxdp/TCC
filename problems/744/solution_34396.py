# a funcao retorna a palavra dada com uma # no inicio, uma # no meio da palavra e uma # no final da palavra
# t e a quantidade de letras da palavra  e s e onde a # vai entrar
# str-> str
def hashtag(s):
    t= len(s)
    return '#' + s[:int(t/2)] + '#' + s[int(t/2):] + '#'