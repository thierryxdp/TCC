def lingua_p(palavra):
    """Função que traduz a palavra de alguma língua normal para a língua p"""
    """Parâmetro de entrada:str"""
    """Parâmetro de saída:str"""
    nova_palavra=''
    for elemento in palavra:
        nova_palavra+=elemento
        if elemento in "AEIOUaeiou":
            nova_palavra+='p'+elemento
    return nova_palavra