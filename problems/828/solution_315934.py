def primo(n):
    "Verifica a primalidade de um número; int->bool"
    l=list(range(1,n))
    r=[+1 for i in l if n%i==0]
    if sum(r)<2:
        return True
    else:
        return False