def soma_impar(n):
    """Função que retorna a soma dos n primeiros numeros ímpares, a partir do n passado como parametro
        int -> int"""
    soma=0
    for i in range(2*n):
        if i%2!=0:
            soma=soma+i
    return soma