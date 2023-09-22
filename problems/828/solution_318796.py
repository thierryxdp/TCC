def primo(n):
    if n==1:
        return False
    aux=0
    for x in range(2,n):
        if n%x==0:
          aux+=1
        if aux==0:
            return True
        else:
            return False