# A função recebe um número inteiro N e retorna o valor da expressão H com 2(duas) casas decimais
# H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N (somatório com N termos)
# int-->float
#
def soma_h(N):
    H=0
    i=1
    while i<=N:
        h=1/i
        H=H+h
        i=i+1
    return round(H,2)