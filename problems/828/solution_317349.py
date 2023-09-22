def primo(numero):
    multiplo=0
    for numero_p in range(1, numero+1):
        if numero%numero_p==0:
            multiplo+=1
        if multiplo==2:
            return True
        else:
            return False