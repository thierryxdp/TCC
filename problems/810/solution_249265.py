def nova_frase(frase):
    '''
    Funcao que recebe uma frase e retorna uma nova frase onde os caracteres de pontuacao '-',',',':',';','.','?','!'
    são substituidos por espaco ' '.
    str -> str
    '''
    f1 = str.join(' ', str.split(frase, '-'))
    f2 = str.join(' ', str.split(f1, ','))
    f3 = str.join(' ', str.split(f2, ':'))
    f4 = str.join(' ', str.split(f3, ';'))
    f5 = str.join(' ', str.split(f4, '.'))
    f6 = str.join(' ', str.split(f5, '?'))
    f7 = str.join(' ', str.split(f6, '!'))
    return f7

# Exercicio 4:
def inverte(frase):
    '''
    Funcao que recebe uma frase e retorna a frase de entrada em ordem inversa sem maiusculas e sem pontuacao.
    str -> str
    '''
    frase_nova = str.lower(nova_frase(frase))
    f1 = frase_nova.split()[::-1]
    f2 = str.join(' ', f1)
    return f2