def primo(x):#funçaõ testa se um número é primo
    if x%2 ==0:#teste se é par
        return False
    for _ in range(3,x,2):#for com passo 2 para reduzir divisões
        if x%_==0:#teste de divisibilidade
            return False
    return True