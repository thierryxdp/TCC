def qtd_divisores(num):
    result=[]
    for div in range(1,num):
        if num%div==0:
            result.append(div)
    return len(result)