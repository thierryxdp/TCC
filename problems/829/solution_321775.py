def soma_h(n):
    """int->float"""
    """H sendo a equação dada no enunciado e o resultado tendo 2 casas decimais"""
    """Função que retorna a equação H com base em qualquer n"""
    
    h=[]
    for i in range(1,n+1):
        list.append(h,1/i)
    return round(sum(h),2)