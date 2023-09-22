def lingua_p(palavra):
    '''Entre com uma palavra para ser retornado a mesma palavra traduzida na
    lingua P
    String -> String'''
    #=========================
    Npalavra=palavra
    x = Npalavra.lower()
    y=len(palavra)
    vogal=["a", "e", "i", "o", "u"]
    #=========================
	
    for i in range(y):
        if i<=y:
            if Npalavra[i] == vogal[i]:
                letra=vogal[i]
                Npalavra.insert(i, "p")
                
    Junta="".join(Npalavra)
          
    return Junta