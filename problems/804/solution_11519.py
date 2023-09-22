def filtra_pares(tupla):
    tuplaVazia = ()
    if tupla[0]%2 == 0:
        tuplaVazia = tuplaVazia + (tupla[0],)
    elif tupla[1]%2 == 0:
        tuplaVazia = tuplaVazia + (tupla[1],)
    elif tupla[2]%2 == 0:
        tuplaVazia = tuplaVazia + (tupla[2],)
    elif tupla[3]%2 == 0:
        tuplaVazia = tuplaVazia + (tupla[3],)
   	return tuplaVazia