def repetidos(num):
    '''função que retorna a quantidade de repetiçoes de um número'''
    '''int-->int'''
    i=1
    lista=[]
    while i<len(num):
        if num[i]==num[i-1]:
            lista+=[lista,num[i]]
        i=i+1
    return len(lista)/2