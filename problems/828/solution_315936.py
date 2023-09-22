def primo(n):
    "Verifica a primalidade de um número; int->bool"
    r=[+1 for i in list(range(1,n)) if n%i==0]
    if sum(r)<2:
        return True
    else:
        return False