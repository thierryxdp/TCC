def total(shopping_list,dict):
    sum=0
    for a in dict.keys():
        if a in shopping_list:
            sum+= dict[a]
            return(sum)