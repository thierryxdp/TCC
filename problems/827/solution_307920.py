def qtd_divisores(numero):
    '''função que verifica quantos divisores um
    número qualquer tem.
    int--> int'''
    
    contador = 0

    for elemento in range(1, numero+1):  #para cada elemento do intervalo 1 até número inserido no parâmetro da função:
        if numero % elemento == 0:  #se divisão do número pelo elemento der zero:
            contador += 1  #incrementa contador
            
    return contador  #retorna contador