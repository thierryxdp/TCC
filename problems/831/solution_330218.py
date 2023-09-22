def lingua_p(palavra):
    """
    
    """
    vogais="aeiouáéíóú"
    linguap=""
    for i in palavra:
        if i in vogais:
            linguap+=i+"p"+i
       	else:
            linguap+=i
  	return linguap