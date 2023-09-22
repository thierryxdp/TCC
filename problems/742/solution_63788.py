# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ dado uma palavra/frase/número, uma caractere qualquer, e um número inteiro.
    vai letra que  está na posição= número e troca ela pelo (caractere qualquer)
    o valor do número inteiro não pode ser maior que a quantidade de caracteres da palvra/frase
    s=str
    x=caractere qualquer
    i=número inteiro
    entrada: str, float ou str, int"""
    h=s[0:i]
    l=s[i:]
    return h+'x'+l