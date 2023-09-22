def filtraMultiplos(lista_num,n):
    '''Função que retorna os múltiplos de um número;
    recebe como parâmetro uma lista com números dada pelu
    usuário e um número,também dado pelo usuário, que 
    determina quem são seus múltiplos da lista dada.
    list,int-->List'''
    i=0
    multiplos=[]
    while i<len(lista_num):
        if(lista_num[i]%n==0):
            list.append(multiplos,lista_num[i])
    	i=i+1
    return multiplos