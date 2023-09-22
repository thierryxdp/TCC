def primo(num):
    primo = bool
    for i in range(2,num):
        if num%i != 0:
            primo = 'True'
        else:
            primo = 'False'
    return primo