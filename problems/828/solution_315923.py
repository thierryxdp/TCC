def primo(numero):
    '''função que verifica se um número 
    qualquer é primo.
    int--> bool'''
    
    contador = 0  #inicia contador em zero
    
    for elemento in range(1, numero+1):  #para cada elemento do intervalo 1 até número inserido no parâmetro da função:
        if numero % elemento == 0:  #se divisão do número pelo elemento der zero:
            contador += 1  #incrementa contador
            
    if contador > 2:  #se contador for maior que 2(tiver mais que 2 divisores):
        return False  #retorna valor booleano Falso
    else:
        return True  #retorna valor booleano Verdadeiro