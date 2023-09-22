def soma_h(N):
    '''Função calcula somatório de frações com N
    termos onde cada fração tem denominador igual
    a posição no somatório. int --> float'''
    soma = [1]
    
    for numero in range(2,N=1):
        soma.append((numero)**-1)
    
    somatorio = sum(soma)
    return round(somatorio,2)