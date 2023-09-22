def lingua_p(palavra):
	vogais=['a','e','i','o','u']    
    palavra.lower()
    palavraINp=''
    for i in palavra:
        if i not in vogais:
            palavraINp+=i
        else:
            palavraINp+=i+'p'+i
    return palavraINp