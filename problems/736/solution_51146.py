def concatenacao(a, b):
    """
    Combina duas strings, a & b, na seguinte ordem: abba.
    str, str -> str

    Parameters:
    a: Parâmetro textual a, do tipo string (str);
    b: Parâmetro textual b, do tipo string (str).
    
    Returns:
    A concatenação de duas strings.
    """
    juncao = (a + b + b + a) 
    return (juncao)