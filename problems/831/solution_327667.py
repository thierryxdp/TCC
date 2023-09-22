def lingua_p(palavra):
    lista=['a','e','i','o','u']
    palavra2=str.lower(palavra)
    for elem in (palavra2):
        if elem in lista:
            palavra2=palavra2[0:elem+1]+'p'+palavra2[elem]+palavra2[elem:]
    return palavra2