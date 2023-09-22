def repetidos(lista):
    """Funçao que receba uma lista de numeros e deve me retornar a quantidade das vezes que existe elementos iguais,
dentro da sua lista. list->int"""
    i = 0
    contagem = 0
    
    while i<len(lista)-1:
        if(lista[i] == lista[i+1]):
            contagem = contagem+1
        i=i+1
    return contagem