def uppCons(frase):
    letra = ''
    vogal = 'a','e','i','o','u'
    while letra < len(frase):
        if frase != vogal:
            frase.upper()
            letra = letra + frase
       	letra = letra + frase
  	return letra