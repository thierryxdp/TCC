def total (lista,precos):	   
    for produtos in lista:	      
        if produtos in precos:	       
            valorTotal=precos[produtos]	   
    return sum(valorTotal)