def lingua_p(palavra):
    """ """
    nova=""
    c=0
    
    for i in range(0,len(palavra)):
        if palavra[i] in "aeiouáéíóúâôêîûãõAÁÉÍÓÚÂÊÎÔÛÃÕEIOU":
            nova = nova + palavra[c:i+1] + "p"
            c=i
            if nova[-1]=="p":
                return nova + palavra[i-1:]
            if nova[-1]not in "aeiouáéíóúâôêîûãõAÁÉÍÓÚÂÊÎÔÛÃÕEIOUp":
                return nova+palavra[-1]