#int->bool
def primo(n):
    "Função que dado um numero inteiro positivo,verifica se esse numero é primo ou nao,e retorna um booleano."
    inicio=1
    divisor=0
    while inicio <=n:
        if n%inicio ==0:
            divisor=divisor +1
        inicio=inicio+1
    if divisor> 2:
        return False
    else:
        return True