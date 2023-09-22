def lingua_p(palavra):
    s = ""
   	for x in list(palavra):
        if x not in 'AEIOUaeiou':
            s + str(x)
        if x in 'AEIOUaeiou':
          	s + str(x)
            s + 'p'
            s + str(x)
    return s