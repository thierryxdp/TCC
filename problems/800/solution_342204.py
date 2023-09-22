def total(shopping_list,dic):
    sum=0
    for a in dic.keys():
        if a in shopping_list:
            sum+= dic[a]
            return(round((sum), 2)