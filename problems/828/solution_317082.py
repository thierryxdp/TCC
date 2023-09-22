def primo(numero):
    ''' '''
    tamanho= numero+1
    lista=[]
    for divisor in range(1,tamanho):
        if numero%divisor==0:
            lista = lista.append(divisor)
        if len(lista) > 2:
            return False
        if len(lista) <=2:
            return True