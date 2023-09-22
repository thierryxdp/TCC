def lingua_p(palavra):
    """essa funcao, dada uma palavra como entrada,
	 retorna a mesma traduzida para lingua do p. apos cada vogal da palavra original,
	 eh inserida a sequencia de letras p mais a vogal original. 
     exemplo -> epexepemplopo
     str -> str """
    
    palavra = list(palavra.lower())
    i = 0
    for x in palavra:
        if x in 'aãâáéeêiíoõôuú':
            soma_string = 'p'+x
            palavra.insert(palavra.index(x, i)+1, soma_string)
        i += 1
    final = ''.join(palavra)
    return final