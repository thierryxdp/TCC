def uppCons(frase):
    """recebe uma frase e retorna a frase com
todas as suas consoantes em maiúsculas e os
demais caracteres exatamente como estavam
str -> str"""
    i = 0
    novafrase = frase[:] #criando um cópia para não modificar a frase atual
    while i < len(frase):
        if frase[i] not in 'ÃAÉEIÍÕOÓÚUãaeéíioõuú': #verificar se não tem vogal
            novafrase = novafrase.replace(novafrase[i],novafrase[i].upper()) #troca pela letra maiscula
            
        i = i + 1
        
    return novafrase