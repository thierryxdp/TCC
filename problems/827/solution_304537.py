def qdt_divisores(numero):
    """Recebe um número inteiro e retorna a quantidade de divisores que este número
       possui.
       int->int

       Parameters:
       numero: O número inteiro no qual se quer descobrir a quantidade de divisores."""
    qdt=0
    for n in range(1,numero+1):
        if numero%n==0:
            qdt=qdt+1
    return qdt