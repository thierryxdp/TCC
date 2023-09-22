def lingua_p(palavra):
    """função que recebe como entrada um palavra e retorna esta mesma palavra traduzida para a língua do P;str->str """
    proximo = 0
    lista = ['a','a','a','e','e','i','o','o','u']
    for i in palavra:
        if lista[proximo] in palavra:
            proximo = proximo + 1
            retorno = str.join('p'+lista[proximo],(str.replace(palavra,lista[proximo],'',1)))
    return  retorno