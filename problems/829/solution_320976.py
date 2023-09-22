def soma_h(n:int) ->float:
    h = 1
    soma = 1
    for i in range(len(n)):
        if i >=2:
            soma += 1/i
    return soma