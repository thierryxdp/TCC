def primo(num):
    '''Uma função dado um inteiro retornar se é primo ou não
    int -> booleano'''
if num < 2: # 0 e 1 não são primos, e vou desconsiderar os números negativos
            return False
elif num == 2: # 2 é o único número par que é primo
    return True
elif num % 2 == 0: # se for par e não é 2, não é primo
    return False
else: # aqui eu sei que o número é ímpar
    # só testo se é divisível por números ímpares
    for i in range(3, num // 2, 2):
        if num % i == 0:
            return False
            break # não é primo, interrompe o for
    else:
        return True