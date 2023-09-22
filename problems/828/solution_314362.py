# Dado um número, quer-se verificar se é primo.
# Resolução:
# 1. Verifica o resto da divisão do número por outro 
#    que seja maior ou igual a 2 ou menor ou igual que sua
#    metade (máximo divisor de n sem ser ele mesmo é n/2);
# 2. Se o resto for 0, adicionar à lista de divisores;
# 3. Verifica o tamanho da lista é 0;
# 4. Se sim, retorna True; se não, False;

def primo(numero: int) -> int:
    '''Dado um número, verifica se é primo'''
    divisores = list()
    for num in range(2, (numero/2) + 1):
        if (numero % num == 0):
            list.append(divisores, num)
    primalidade = (len(divisores) == 0)
    return primalidade