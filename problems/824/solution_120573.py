def uppCons(s)
	"""Dada uma frase de entrada, retorna a mesma frase com todas as consoantes reescritas
maiúsculas (mantendo os demais caracteres da frase originais).
Assinatura: str -> str
Casos de teste:
uppCons('victor') = 'ViCToR'
uppCons('gabriel') = 'GaBRieL'
"""
    vogais = ['a', 'á', 'à', 'ã', 'â', 'e', 'é', 'ê', 'í', 'ó', 'ô', 'õ', 'ú']
    fr_s = list(s)
    for l in range(len(fr_s)):
        if not fr_s[l] in vogais:
            fr_s[l] = str.upper(fr_s[l])
	return str.join('', fr_s)