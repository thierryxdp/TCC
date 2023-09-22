def lingua_p(palavra):
    """Traduz a palavra para a lingua do p
       string --> string"""
    vogal = ("aeiou")
    
	for i in range(len(palavra)):
        if palavra[i] == vogal:
    		return palavra[i] + "p" + palavra[i]