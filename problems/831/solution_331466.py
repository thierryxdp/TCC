def lingua_p(palavra):
	"""Recebe uma palavras e a retorna traduzida para a lingua do p; str->str.""" 
    palavra=str.lower(palavra)
    for letra in palavra:
		palavra_traduzida= letra+"p"
	return palavra_traduzida