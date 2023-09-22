def lingua_p(palavra):
    """Função que traduz a palavra de alguma língua normal para a língua p"""
    """Parâmetro de entrada:str"""
    """Parâmetro de saída:str"""
    nova_palavra=''
    for elemento in palavra:
        if elemento in "AEIOUaeiou":
            nova_palavra=elemento+'p'+elemento
        else:
			nova_palavra+=elemento
    return nova_palavra