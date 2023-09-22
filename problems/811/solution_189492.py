''' calcula e retorna se o colchão passa ou não pela porta q tem altura de 200 cm e 100 cm de largura
tendo em vista q o colchão é no formato axbxc.
Entrada: Os parâmetros de entrada são uma lista com as dimensões do colchão em centímetros, ordenadas da menor para a maior, e dois inteiros H e L, correspondentes respectivamente a altura e a largura das portas em centímetros.
Retorno: true se passar pela porta, false caso n passe'''
def colchao(c,h,l):
    if c[1] > h and c[2] > l:
        return False
    elif c[1] <= h:
        return True
    else:
        return False