def total(lista,dic):
    sum=0
    for a in dic.keys():
        if a in lista:
            sum+= dic[a]
            return(sum)