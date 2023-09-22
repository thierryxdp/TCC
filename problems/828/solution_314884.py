def primo(x):
    'verifica se o numero dado é ou não é primo inr -> true/false'
    k=2
    primo = x
    while(x%k != 0) or k<=x:
        k=k+1
        return x == primo
    else:
        return x != primo