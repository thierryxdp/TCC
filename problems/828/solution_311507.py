def primo(numero):
    '''Dado um número inteiro e positivo, verifica se este número é primo
    ou não.

    obs: como 2 é o único número primo par, quando recebe outro número par
    a função retorna False direto e, para números ímpares, só verifica
    divisões por denominadores ímpares. 

    int -> bool'''

    par = numero%2 == 0
    
    if numero != 2 and par:
        return False

    numDivisores = 0
    
    for elemento in range(1,numero+1,2):
        if numero%elemento == 0:
            numDivisores = numDivisores + 1

    eh_primo = numDivisores <= 2

    return eh_primo