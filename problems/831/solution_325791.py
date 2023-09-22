def lingua_p(palavra):
    s = ""
   	for x in len(palavra):
        if x not in 'AEIOUaeiou':
            s + str.lower(str(x))
        if x in 'AEIOUaeiou':
          	s + str.lower(str(x))
            s + 'p'
            s + str.lower(str(x))
    return s