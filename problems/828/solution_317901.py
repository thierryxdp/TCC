def primo(n):
    '''it returns if n is a prime number or not
    int -> value boolean'''
    otherdivisors=0
    for intenger in [range(1:n)]:
        if n%intenger==0:
            otherdivisors+=1
    return if otherdivisors=0