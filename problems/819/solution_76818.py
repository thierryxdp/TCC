def filtraMultiplos(lista_num, numero):
    """Recebe uma lista de números e um número inteiro, retorna uma lista 
       contendo todos os número da lista original que são multiplos do número
       inteiro 
       list, int ->list
       
       Parameters:
       lista_num: Uma lista de números.
       
       numero: Um número inteiro."""
    
    i=0
    multiplos=[]
    while i<len(lista):
        if lista_num[i]%numero==0:
            list.append(multiplos,lista_num[i])
        i=i+1
    return multiplos