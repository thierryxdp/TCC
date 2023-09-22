def filtra_pares(numeros):
    """calcula e retorna somente os elementos pares dos quatro numeros inteiros de entrada presentes na tupla, na mesma ordem em que eles se encontravam;
    int, int, int, int-> tuple"""
    numero1,numero2,numero3,numero4=numeros
    tupla_saida=()
    if (numero1)%2==0:
        tupla_saida=tupla_saida+(numero1,)
    if (numero2)%2==0:
        tupla_saida=tupla_saida+(numero2,)
    if (numero3)%2==0:
        tupla_saida=tupla_saida+(numero3,)
    if (numero4)%2==0:
        tupla_saida=tupla_saida+(numero4)
        return tupla_saida