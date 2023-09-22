def primo(numero):
    i=1
    valor=[]
    while i<=numero:
        if numero%i==0:
            list.append(valor,i)
        i=i+1
    if len(valor)==2:
        return 'True'
    else:
        return 'False'