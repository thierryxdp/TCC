def qtd_divisores(n_1:int)->int:
    if n_1<0:
        return 0
    def is_divisor(n_2:int)->bool:
        return True if n_1%n_2 == 0 else False
    return len(list(filter(is_divisor,range(1,n_1//2+1))))+1