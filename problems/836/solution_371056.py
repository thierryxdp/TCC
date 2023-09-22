def busca(contatos, palavra):
    '''Função que retorna a lista do "nome" do contato que está inserido, de entrada: list, str -> list'''

    contato = [ ]
    indice = 0

    for indice in range(len(contatos)):
        if palavra.lower( ) in contatos[indice][0].lower( ):
            contato.append(contatos[indice])
        indice += 1
    else:
        indice += 1
    
    return contato