def inverte(frase):
    '''funcao que dado uma frase retorna essa mesma frase na ordem inversa
    e sem nenhuma pontuacao; str -> str'''
    lista = str.split(frase)
    inverter = lista[::-1]
    
    return inverter