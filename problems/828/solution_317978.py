def primo(n):
    """Função que retorna se um dado número inteiro é primo ou não;
int -> bool"""
    divisores=list(range(1,n+1))
    lista=[]
    for numero in divisores:
        if n%numero==0:
            lista.append(numero)
    if len(lista)>2:
        return False
    else:
        return True