def lingua_p(palavra):
    palavra=palavra.lower
    for i in palavra:
        if i in "aeiou":
    		palavra = palavra[0:i+1]+"p"+i+palavra[i+1]
    return palavra