def lingua_p(palavra):
    palavra.lower
    palavranova=()
    for i in range(len(palavra)):
        if palavra[i] in "aeiou":
    		palavranova = palavra[0:i+1]+"p"+palavra[i]
  
    return palavranova