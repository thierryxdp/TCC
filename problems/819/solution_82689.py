def filtraMultiplos(l,n):
    '''retorna uma lista com os elementos da lista original
    que são divisíveis por n
    list, int -> list'''
    #contador
    i=0
    #acumulador - lista com múltiplos de n 
    multiplosn=[]
    #condição de parada: varrer toda a lista de entrada (l)
    #ação que se repete: verificar para cada elemento se é divisível por n (l[i]%n==0) 
    while (i<len(l)):
        if l[i]%n==0:
            multiplosn.append(l[i])
            #list.append(multiplosn,l[i])
        i+=1
    return multiplosn