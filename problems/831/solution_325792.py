def lingua_p(palavra):
    s = ""
    lista = list(palavra)
   	for x in lista:
        if x not in 'AEIOUaeiou':
            s + str.lower(str(x))
        if x in 'AEIOUaeiou':
          	s + str.lower(str(x))
            s + 'p'
            s + str.lower(str(x))
    return s