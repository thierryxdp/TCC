def primo(n):
    div = 2
    x = True
    if n == 2:
        return True
    elif n > 2:
        while div < n:
            if n % div == 0:
                x = False
            div += 1
    return x
#Números primos são aqueles divisíveis apenas por 1 e por eles mesmos
#Minha variavel div = atribui o valor 2
#Se o parametro n for igual a 2
#Retorma verdadeiro
#Caso n maior que 2, enquanto div < que n, se n (reso de divisão) igual a 0
#Meu x é falso
#div += 'retorna verdadeiro