def soma_h(n):
    '''Calcula a soma de n termos de h'''
    h = 1
    denominadores = list(range(2,n+1))#lista com os denominadores
    denominador = 0
    for denominador in denominadores:
        h = h + 1/denominador #Soma dos termos
    return round (h,2)