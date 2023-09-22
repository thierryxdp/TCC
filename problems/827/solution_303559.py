def qtd_divisores(num):
    """Funcao recebe um numero e retorna a quantidade de divisores que ele tem. int->int"""
    lista2=[]
    for div in range(1,num+1):
        if num%div==0:
            lista2.append(div)
    return len(lista2)