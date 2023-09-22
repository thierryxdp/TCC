def soma_h(n:int) ->float:
    
    soma = 0
    for i in range(n):
        if i >=1:
            soma += 1/i
    return round(soma, 2)