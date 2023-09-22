def qtd_divisores(n):
   """ Código que cálcula quantidade de divisores para um n dado
   
   :n --> int:
   :return --> qtd:
   """ 
    qtd = 0
    for i in range(1,n +1):
        if n%i == 0:
            qtd += 1
            
    return qtd