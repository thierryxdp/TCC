def lingua_p(palavra):
    palavra.lower
    palavranova=palavra
    for i in range(len(palavra)):
        if palavra[i] in "aeiou":
    		palavranova = palavranova[0:i+1]+"p"+palavra[i]
        else:
            palavranova=palavranova[0:i]+palavra[i]
            
    return palavranova