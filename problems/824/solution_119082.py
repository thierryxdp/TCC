def uppCons(texto):
#vai receber uma frase e vai retornar as consoantes maisuculas
#e as vogais vão ficar como estavam
	fn = " "
	for e in texto:
        if e in 'bcdfghjklmnpqrstvwxyzç':
            fn += str.upper(e)
		else:
            fn += e
		return fn