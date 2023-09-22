def filtra_pares(t1):
   def ss(s):
    """Função que recebe uma string(s), um caractere(x) e um numero(i) entra 0 e o comprimento da string
    retornando, a string "s", sendo trocado o elemento da posição "i" pelo caractere "x";
    str, str, int -> str"""
    valor1 = s[0]
    valor2 = s[1]
    valor3 = s[2]
    valor4 = s[3]
    if valor1%2 == 0 and not (valor2,valor3,valor4%2) == 0:
        return valor1 
    elif valor2%2 == 0 and not (valor1,valor3,valor4%2) == 0:
        return valor2
    elif valor3%2 == 0 and not (valor1,valor2,valor4%2) == 0:
        return valor3
    elif valor4%2 == 0 and not (valor1,valor2,valor3%2) == 0:
        return valor4
    elif valor1%2 == 0 and valor2%2 == 0 and (valor3,valor4%2) !=0:
        return valor1,valor2
    elif valor1%2 == 0 and valor3%2 == 0 and (valor2,valor4%2) !=0:
        return valor1,valor3
    elif valor1%2 == 0 and valor4%2 == 0 and (valor2,valor3%2) !=0:
        return valor1,valor4
    elif valor2%2 == 0 and valor3%2 == 0 and (valor1,valor4%2) !=0:
        return valor2,valor3
    elif valor2%2 == 0 and valor4%2 == 0 and (valor1,valor3%2) !=0:
        return valor2,valor4
    elif valor3%2 == 0 and valor4%2 == 0 and (valor1,valor2%2) !=0:
        return valor3,valor4
    elif (valor1,valor2,valor3)%2 == 0 and valor4%2 !=0:
        return valor1,valor2,valor3
    elif (valor1,valor2,valor4%2) == 0 and valor3%2 !=0:
        return valor1, valor2, valor4
    elif (valor1,valor3,valor4%2) == 0 and valor2%2 !=0:
        return valor1, valor3, valor4
    elif (valor2,valor3,valor4%2) == 0 and valor1%2 !=0:
        return valor2,valor3,valor4
    else: