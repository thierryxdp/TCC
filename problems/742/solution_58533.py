# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    #A função identifica o termo especificado, separa em duas strings e troca o caractere
    I, R = s[:i], s[i+1:]
    saida = I + x + R
    return saida