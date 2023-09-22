def lingua_p(palavra):
    lista=['a','e','i','o','u']
    palavra2=str.lower(palavra)
    i=0
    k=len(palavra2)
    for elem in (palavra2):
        while i<k:
            if elem in lista:
                palavra2=palavra2[0:i]+'p'+palavra2[i]+palavra2[i:]
    return palavra2