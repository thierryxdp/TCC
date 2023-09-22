def uppCons(frase):
    vogal = 'a','e','i','o','u'
    fraseNew = ''
    while i < len(frase):
        if frase == vogal:
            fraseNew = fraseNew + frase
        fraseNew = fraseNew.upper()
  	return fraseNew