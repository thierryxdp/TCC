def fatorial(N):
    """dado um número N inteiro, calcula o fatorial desse número (int --> int) """ """valores float ou complex
    resultaram na função não funcionando"""
    produto = 1 #defini-se o acumulador
    i = 1 #define-se o contador
    while i <= N : #repete-se os comandos da linha 7 e 8 enquanto o contador não superar o número N
        produto = produto * i  #aqui multiplica-se o acumulador pelo inteiro i
        i = i+1 #aumenta-se o valor do contador
    return produto #retona o fatorial do número N