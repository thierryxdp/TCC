#Função que verifica se o número dado como entrada é primo ou não,é necessário que seja positivo, int = int
def primo(p):
    conta= 0

    for divisor in range(1,p+1):
        if p%divisor ==0:
           conta = conta + 1
    if conta ==2:
        return True
    else:
        return False