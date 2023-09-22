def filtraMutiplos(lista, numero):
    ''' a função tem por objetivo verificar se os números
da lista são multiplos da variável número. recebe uma lista e retorna uma lista como resultado''' 
    resultado=[]
    x=0
    while x <= len(lista)-1:
        if lista[x] % numero == 0:
            y = lista[x]
            list.append(resultado,y)
            x = x + 1
        elif lista[x] <= len(lista):
            lista[x]% numero != 0
            x= x+1
        
    return resultado