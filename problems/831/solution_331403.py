def lingua_p(palavra):
    palavra.lower
    palavranova=""
    for i in range(len(palavra)):
        if palavra[i] in "aeiou":
            palavranova = palavranova[0:(len(palavranova))+1]+"p"+palavra[i]
        else:
            palavranova=palavranova[0::]+palavra[i]
    return palavranova