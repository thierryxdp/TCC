def lingua_p(frase):
    '''Função que recebe uma frase e retorna uma nova frase com
a linguagem p
Entrada(string)
Saida(string)'''
    #variavel vazia(acumulador)
    novafrase=''
    #loop para verificar cada letra
    for i in range(0,len(frase)):
        #condicao para saber se a letra é uma consoante,e se nao for adicionar a letra p
        if str.lower(frase[i]) not in 'qwrtypsdfghjklzxcvbnm':
            novafrase+=frase[i]+'p' + frase[i]
        else:
            novafrase+=frase[i]
    return novafrase