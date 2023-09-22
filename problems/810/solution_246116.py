def retira_pontuacao(texto):
	"""Substitui todas as pontuações de um dado texto por espaços, retornando uma nova frase sem espaços.
    Entrada: str
    Saída: str
    """
	A = str.replace (texto, '-', ' ')
	B = str.replace (A, ',', '')
	C = str.replace (B, ':', '')
	D = str.replace (C, ';', '')
	E = str.replace (D, '.', '')
	F = str.replace (E, '!', '')
	G = str.replace (F, '?', '')
	return G

def inverte (texto):
    """Inverte uma dada frase, sem letras maiúsculas e sem pontuação.
    Entrada: str
    Saída: str
    """
    H = str.lower (texto)
    I = retira_pontuacao (H)
    J = str.split (I)
    K = list.reverse (J)
    return str.join(' ', J)