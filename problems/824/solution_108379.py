def uppCons(frase):
    """Recebe como entrada uma frase e retorna a frase com todas as suas consoantes em maiúsculas
    (str --> str)""" """a função funciona somento com strings, colocar outro tipo de dado resultará em erro"""
    frase_ajustada = frase #cria-se um alias da frase inserida para podermos alterá-la
    i = 0  #define-se o contador
    consoantes = "bcçdfghjklmnpqrstvwxyz" #cria-se a string consoantes, ela será usada para procurar as consoantes dentro da frase. Vale ressaltar que não foi incluído consoantes maiúsculas, isso ocorre pois não é necessário reconhecer consoantes maiúsculas já que não iremos alterá-las
    while i < len(frase) : #repete-se os comandos da linha 8 a 10 enquanto i for menor que o comprimento da string frase, ou seja, o processo será repetido para todos as posições de frase
        if frase_ajustada[i] in consoantes: #checa-se se a posição i de frase é uma consoante
            frase_ajustada = frase_ajustada[:i] + str.upper(frase_ajustada[i]) + frase_ajustada[i+1:] #sendo a posição i uma consoante, ela é substituída por string com a mesma letra, só que maiúscula
        i = i+1 #aqui se aumenta o valor do contador para repetir o processo com a próxima posição da string frase
    return frase_ajustada #se retorna a frase com a alteração desejada.