def primo(numero):
    """Função que recebe um numero como parâmetro e retorna em bool se esse número é primo ou não.Entrada -> int; Saída -> bool"""
    divisores = []
    for divisor in range(1, numero+1):
        if numero % divisor ==0:
            divisores = divisores + [divisor,]
    if len(divisores)>2:
        return bool(0)

    if len(divisores)<=2:
        return bool(1)