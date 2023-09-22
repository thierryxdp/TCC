'''Função que recebe uma lista de inteiros ordenados na ordem crescente e um
inteiro e retorna uma nova lista com os elementos da lista inicial e o inteiro 
dado na ordem correta para que a nova lista continue na ordem crescente.'''
def insere(lista,n):
    z=0
    teste = False
    for x in lista:
        z+=1
        if n <x:
            teste = True
            lista.insert(z-1,n)
            break
    if teste == False:
        lista.append(n)
    return lista