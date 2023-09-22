#map
def f(x):
    '''calcula 1/x; int -> float'''
    return 1/x

def soma_h(n):
    '''retorna a soma de n termos de 1+1/2+...+1/n; int -> float'''
    lista=list(map(f,list(range(1,n+1))))
    return sum(lista)