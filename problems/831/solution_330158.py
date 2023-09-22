def lingua_p(palavra):
    #Deixando toda a string em caixa baixa
    palavra = str.lower(palavra)
    #Pegando cada letra da string
    for letra in palavra:
        if letra in 'aeiou':
            i = str.find(palavra,letra)
            palavra = palavra[0:i] +'p' + palavra[i:]
	return palavra