def lingua_p(palavra):
    palavra=palavra.lower
    for i in range(len(palavra)):
        if palavra[i] in "aeiou":
    		palavra = palavra[0:i+1]+"p"+palavra[i]+palavra[i+1]
    return palavra