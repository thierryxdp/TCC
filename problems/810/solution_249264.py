'''
Funcao que recebe uma frase e retorna a frase de entrada em ordem inversa sem maiusculas e sem pontuacao.
str -> str
'''
def inverte(frase):
    frase_nova = str.lower(nova_frase(frase))
    f1 = frase_nova.split()[::-1]
    f2 = str.join(' ', f1)
    return f2