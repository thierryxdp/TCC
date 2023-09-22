def qtd_divisores(num):
    """  """
    div=[]
    for n in range(1,num+1):
        if num%n==0:
            div.append(n)
    return len(div)