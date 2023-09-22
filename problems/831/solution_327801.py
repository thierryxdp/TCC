def lingua_p(palavra):
    '''Entre com uma palavra para ser retornado a mesma palavra traduzida na
    lingua P
    String -> String'''
    #==============================
    Y=len(palavra)
    vogal=["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    Nlista=[]
    #==============================     
    for i in range(Y):
        if i<=Y:
            if palavra[i] in vogal:
                letra=palavra[i]
                Nlista=Nlista+[letra, ]
                Nlista=Nlista+["p", ]
                Nlista=Nlista+[letra, ]
            else:
                letra=palavra[i]
                Nlista=Nlista+[letra, ] 
                
    Junta="".join(Nlista)
    return Junta