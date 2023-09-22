def lingua_p(palavra):
    """ """
    nova=""
    c=0
    
    for i in range(0,len(palavra)):
        if palavra[i] in "aeiouáéíóúâôêîûãõAÁÉÍÓÚÂÊÎÔÛÃÕEIOU":
            nova = nova + palavra[c:i+1] + "p"
            c=i
            
           
    return nova+palavra[-1]