def primo(n):
    '''it returns if n is a prime number or not
    int -> value boolean'''
    otherdivisors=0
    auxiler_list= list(range(1:n))
    for intenger in auxiler_list:
        if n%intenger==0:
            otherdivisors+=1
    return if otherdivisors=0