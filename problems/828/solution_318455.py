def primo(num):
    """funcao que dado um numero inteiro positivo, verifica
se este numero e primo ou nao
int -> bool"""
    divisores = []
    for i in range(1,num+1):
        if num%i == 0:
            list.append(divisores,i)
    return divisores == [1,num]