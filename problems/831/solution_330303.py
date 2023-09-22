def lingua_p(palavra):
    """Retorna a palavra dada na língua do P;
str -> str"""
    proximo = 0
    palavra = str.lower(palavra)
    palavra2 = []
    
    while proximo < len(palavra):
        if palavra[proximo] not in "aeiouáéíóú":
            palavra2 += [palavra[proximo],]

        if palavra[proximo] in "aeiouáéíóú":
            palavra2 += [palavra[proximo]+"p"+palavra[proximo]]
           
        proximo += 1    
                 
    return str.join("",palavra2)