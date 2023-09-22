"junção da entrada de duas strings com a inversa delas mesmas"
" a e b"
"str, str => str"
def concatenacao(a , b):
    str1 = a
    str2 = b
    str3 = (str1 +str2)

    return str3 + str3[-1::-1]