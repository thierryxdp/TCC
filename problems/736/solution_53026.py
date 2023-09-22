# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a , b):
    str1 = a
    str2 = b
    str3 = (str1 +str2)

    return str3 + str3[-1::-1]