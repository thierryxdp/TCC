"retorna a junçao de duas strings com a juncao das duas de tras para frente"
"a e b"
"str, str -> str"
def concatenacao(a , b):
    str1 = a
    str2 = b
    str3 = (str1 +str2)

    return str3 + str3[-1::-1]