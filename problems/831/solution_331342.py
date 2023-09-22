def lingua_p(palavra):
    '''str -> str'''
    x=''
    palavra=str.lower(palavra)
    i=0
    for vogal in palavra:
        if vogal not in 'aeiouáéíúóãõêô':
            x+=palavra[i]
        if vogal in 'aeiouáéíúóãõêô':
            x+=vogal+'p'+vogal
        i+=1
    return x