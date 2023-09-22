def concatenacao(a, b):
    """Função que, dadas duas strings 'a' e 'b', nos retorna a concatenação delas no formato 'abba'
    
    (str, str) -> (str)
    """
    
    return a + b*2 + a


def teste_concatenacao():
    """Função que testa a veracidade da função concatenacao(a, b)"""
    
    print(concatenacao("oi", "prof") == "oiprofprofoi")
    print(concatenacao("machine", "teaching") == "machineteachingteachingmachine")
    print(concatenacao("haha", "hoho") == "hahahohohohohaha")