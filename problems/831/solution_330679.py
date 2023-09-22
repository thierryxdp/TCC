def lingua_p(palavra):
    '''função que recebe palavra em português e
    retorna palavra traduzida em língua do p.
    str--> str'''
    
    traduzido_p = []  #cria lista vazia para a tradução
    contador = 0  #inicia contador em 0

    for letra in list(palavra):  #para cada letra da palavra inserida no parâmetro da função:
        if letra in 'aeiouáéíóú':  #se letra for uma vogal com ou sem acento
            traduzido_p.append(letra + 'p' + letra)  #insere p e a vogal na lista
        else:  #se não for vogal
            traduzido_p.append(letra)  #insere letra sem p na lista

    return ''.join(traduzido_p)  #junta elementos da lista para formar a palavra