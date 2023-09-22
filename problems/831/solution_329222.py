def lingua_p(palavra):
    
    for i<len(palavra):
        if palavra[i] in "aeiouAEIOU":
            b="p"+str(palavra[i])
            return palavra[i]+"p"+str(palavra[i])