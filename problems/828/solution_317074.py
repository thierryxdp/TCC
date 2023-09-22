def primo(numero):
    tamanho= numero+1
    lista=[]
    for divisor in range(1,tamanho):
        if numero%divisor==0:
            lista.append(divisor)
       	if numero and 1 in lista:
            return True