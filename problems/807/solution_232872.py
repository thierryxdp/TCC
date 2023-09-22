def n(frase):
    quantidade = 0
    for i in range(len(frase)):
        if i in ['.','?','!','...']:
            quantidade+=1
            return quantidade