"""A função concatena a lista 'y' e organiza ela em ordem crescente,
usando index se acha em qual indice o "y" está na lista e recorta os elementos 
que estão atras dele

list + int --> list"""
def maiores(x,y):
    list.append(x, y)
    x.sort()
    A= x.index(y)
    return x[A+1:]