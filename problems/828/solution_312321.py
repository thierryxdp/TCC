def primo(n):
    def qtd_divisores(n):
        soma=0
        for i in range(1,n+1):
            if n%i==0:
                soma+=1
        return soma
    if qtd_divisores(n)!=0:
        return False
    else:
        return True