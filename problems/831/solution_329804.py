def lingua_p(palavra):
    palavra.lower()
    palavraF=' '
    
    for i in palavra:
        if i in 'aeiou':
            palavraF += i+'p'+i
        else:
            palavraF += i
    return palavraF