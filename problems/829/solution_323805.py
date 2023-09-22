def soma_h(N):
    '''fun ̧cao calcula somatorio de fra ̧coes com
N termos onde cada fra ̧cao tem denominador igual
a sua posi ̧cao no somatorio.
int--> float'''
    lista_soma = [1]
    
    for numero in range(2, N+1):
        lista_soma.append((numero)**-1)
        
    somatorio = sum(lista_soma)
        
    return round(somatorio, 2)