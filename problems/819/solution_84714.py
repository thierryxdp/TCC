def filtraMultiplos(l,n):
    ''' Essa função que dada uma tupla não vazia de inteiros, retorna uma tupla com os inteiros que forem multiplos do termo também dado;
    Recebe lista e um número;
    Retorna uma lista com os numeros da lista original que são multiplos do número dado.
    tuple --> tuple'''
    listafinal = ()
    ini = 0
    while ini <len(l):
        if l[ini]%n == 0:
            listafinal = listafinal + (l[ini],)
        ini = ini + 1
    return listafinal
#Essa função que dada uma tupla não vazia de inteiros, retorna uma lista com os numeros da lista original que são multiplos do número dado.