def total(lista,dict):
    sum=0
    for a in dict.keys():
        if a in lista:
            sum+= dict[a]
            return(sum)