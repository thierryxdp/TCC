def primo(numero):
    "Função que verifica se um número dado de entrada é primo. int --> bool"
    mults=0
    for i in range(2,numero):
        if numero%i==0:
            mults+=1
    if mults==0:
        return True
    else:
        return False