def lingua_p(palavra):
	"""Função em que dada um string palavra (em português) retorna esta palavra traduzida para a língua do P toda em minúscula. Língua tal em que  após cada vogal de um palavra na língua portuguêsa é posto em sequência a letra p e a vogal anterior ao p.
	string -> string."""
	palavra.lower()
	p=list(palavra)
	k=[]
	for x in p:
		list.append(k,x)
		if x in 'aeiou':
			list.append(k,'p')
			list.append(k,x)
	return ''.join(k)