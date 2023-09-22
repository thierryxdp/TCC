def lingua_p(palavra):
	"""Recebe uma palavras e a retorna traduzida para a lingua do p; str->str.""" 
    palavra=str.lower(palavra)
    i=0
    palavra_traduzida=" "
    for letra in palavra:
        palavra_traduzida+= palavra[i]+"p"
        i+=1
        palavra_traduzida+=palavra[i]
        i+=1
	return palavra_traduzida