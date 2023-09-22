def primo(n):
    '''it returns if n is a prime number or not
    int -> value boolean'''
    otherdivisors=0
    for intenger in list(range(n))[2:n]:
        if n%intenger==0:
            otherdivisors+=1
    return otherdivisors==0