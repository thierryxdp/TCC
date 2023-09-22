def primo(numero):
    """Função que diz se um numero é primo ou não, na entrada ela recebe um número inteiro e na saída ela 
    retorna um valor booleano"""
    contagem=0
    for item in range(1,numero+1):
        if numero%item ==0:
            contagem+=1
    if contagem ==2:
        return True
    else:
        return False