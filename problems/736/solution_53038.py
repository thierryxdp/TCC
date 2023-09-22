def concatenacao(a , b):
    "junção da entrada de duas strings com a inversa delas mesmas"
    " a e b"
    " str, str => str"
    str1 = a
    str2 = b
    

    return (str1 + str2) + str1[-1::-1] +str2[-1::-1]