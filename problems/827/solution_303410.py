def qtd_divisores(num):
    """Funcao recebe um numero e retorna a quantidade de divisores que ele tem. int->int"""
    lista2=[]
    div=1
    while div<=num:
        if num%div==0:
            lista2.append(div)
        div=div+1
    return len(lista2)