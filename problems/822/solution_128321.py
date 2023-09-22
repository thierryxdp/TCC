def repetidos(ls):
    lst=ls[1:]
    p=0
    for i in lst:
        if ls[i]==lst[i]:
            p+=1
    return p