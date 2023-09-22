#Entrada: Um número inteiro e positivo
#1 - Precisamos saber a quantidade de divisores desse número
#1.1 - se for maior que 2, então não é primo
#2 - Retornar se o número é prim ou nao
def primo(numero: int)->bool:
    """Recebe um número e diz se ele é primo ou não"""
    qntDivisores=0
    for n in range(1,numero+1):
        if numero%n==0:
            qntDivisores+=1
    if qntDivisores > 2:
        return False
    else: 
        return True