def qnt_divisores(num):
    """
    	Retorna quantos divisores o número informado possui
        int -> int
    """
    tot_divisores = 0
    for i in range(1,num+1):
        if num%i==0:
            tot_divisores+=1
    return tot_divisores