def primo(N):
    """dado um número inteiro positivo (isso exclui zero), verifica a primalidade do número
    (int --> boolean)""" """
    Se um número Z não é primo, ele pode ser fatorado em dois fatores A e B, temos então que Z = A * B. 
    Sabemos que sqrt(A) * sqrt(B) = Z, ou seja, se ambos A e B fossem maiores que a raiz quadrada de Z, teríamos que
    sqrt(A) * sqrt(B) > Z, o que não é verdade.
    Portanto, concluímos que ambos A e B não podem ser maiores que a raiz quadrada de Z.
    Então, em qualquer fatorização de Z em dois termos, temos que os dois termos não podem ser, simultaneamente,
    maiores que sqrt(Z)
    Agora, imaginemos o primeiro caso: Z pode ser expresso na forma de um produto de dois números naturais (P * R). Temos
    então que P <= sqrt(Z) e Q <= sqrt(Z).
    Segundo caso: Z pode ser expresso na forma de um produto de n números (Q*W*...*R*T). Realizando as
    multiplicações, chegamos em Z = H * T, onde H = Q*W*...*R. Dessa forma, T <= sqrt(Z) e H <= sqrt(Z). Como H é
    um produto de números naturais, concluímos que os números Q, W, ... são menores que H. Assim, todos os fatores
    são menores ou iguais a sqrt(Z)."""
    """Disso tudo, concluímos que pelo menos um dos fatores de um número primo tem de menor ou igual a raíz quadrada
    desse mesmo número primo. Isso nos possibilita criar um algoritmo que precisa checar menos números quando
    realiza um teste de primalidade, só precisamos checar de 2 até o maior número natural menor que a raíz
    quadrada do número que submetemos ao teste de primalidade"""
    Num_de_div = 0 #cria-se o acumulador
    LIM = round(N ** (1/2))+ 1 #calcula-se o maior número natural menor que a raíz quadrada do número que submetemos ao teste de primalidade.Em seguida, definimos LIM de forma que list(range(2,LIM)) nos forneça uma lista que vá de 2 até o maior número natural menor que a raíz quadrada de N 
    lista_de_num = list(range(2,LIM)) #cria-se-se a lista de 2 até o maior número natural menor que sqrt(N)
    for numero_i in lista_de_num : #repete-se os comandos nas linhas 24 e 25 para todos os elementos da lista_de_num
        if N % numero_i == 0 : #se N for divisível por numero_i da lista, é adicionado 1 ao Num_de_div
            Num_de_div = Num_de_div +1
    if Num_de_div == 0 : #Como a lista começa em 2, números primos não teram divisores presentes na lista, portanto, se Num_de_div == 0, N é primo
        return True
    else:
        return False #Caso contrário, N não é primo