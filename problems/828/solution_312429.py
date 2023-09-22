def primo(numero):
    """Recebe um número inteiro positivo e retorna True se ele for um número primo
       e False se não form um número primo.
       int->bool

       Parameters:
       numero: Um número inteiro positivo."""
    qdt_div=0
    for n in range(1,numero+1):
        if numero%n==0:
            qdt_div=qdt_div+1
    if qdt_div==2:
        return True
    else:
        return False