def filtraMultiplos(lis,num):
    ''' Função que retorna todos os elementos contidos 
        em 'lis' list,int -> list'''
    div = []
    ele = 0
    while ele < len(lis):
        if lis[ele] % num == 0:
            div += (lis[ele] ,)
            ele += 1
        return div