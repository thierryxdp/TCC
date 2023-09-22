def primo(numero):
    proximo=2
    lista=[]
    for proximo in range(2,9):
         if numero%proximo==0:
            lista += [proximo]
            proximo += 1
            return len(lista)