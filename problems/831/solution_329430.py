def lingua_p(palvra):
    """Função que traduz a palavra de alguma língua normal para a língua p"""
    """Parâmetro de entrada:str"""
    """Parâmetro de saída:str"""
    nova_palavra=''
    for elemento in palavra:
        if elemento in "AEIOUaeiou":
            nova_palavra+"p"+elemento+"p"
        else:
			nova_palavra+=elmento
    return nova_palavra