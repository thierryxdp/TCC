def soma_h(N):
    """De acordo com a série H = (1 + 1/2 + 1/3 + 1/4 +
+ ... + 1/N) retorna o valor de H com N termos, sendo N
o número inteiro positivo recebido na entrada da função.
int -> float
"""
    ls_atual = []
    for i in range(1,N+1):
        list.append(ls_atual, 1/i)    
    return round(sum(ls_atual), 2)