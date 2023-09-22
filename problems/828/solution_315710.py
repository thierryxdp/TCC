def primo(num):
    primo = bool
    for i in range(0,num):
        if num%i == 0:
            primo = 'False'
        else:
            primo = 'True'
    return primo