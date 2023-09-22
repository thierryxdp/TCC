def lingua_p(palavra):
    lista=['a','e','i','o','u']
    palavra2=str.lower(palavra)
    for elem in (palavra2):
        for n in range(palavra2+1):
            if elem in lista:
                palavra2=palavra2[0:n+1]+'p'+palavra2[n]+palavra2[n:]
    return palavra2