def maiores(lista,n):
    maiores_que_n=[]
    for i in lista:
        if i>n:
            maiores_que_n+=i
        else:
            None
    return list.sort(maiores_que_n)