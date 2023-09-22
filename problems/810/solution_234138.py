def inverte (frase):
    '''função que retorna as palavras de uma frase na ordem inversa, sem pontuação e sem letras maiúsculas.
    string -> string'''
    ### Remover pontuação
    travessao = str.replace(frase, '-', ';')
    virgula = str.replace(travessao, ',', ';')
    doispontos = str.replace(virgula, ':', ';')
    pontoevirgula = str.replace(doispontos, ';', ' ')
    sempontofinal= pontoevirgula[0:len(pontoevirgula)-1]+ ' '
    
    ### Remover letras maiúsculas
    minuscula = str.lower(sempontofinal)
    
    ### Separar as palavras
    palavras = str.split (minuscula)
    
    ### Juntar em ordem reversa
    return str(palavras)[-1:]