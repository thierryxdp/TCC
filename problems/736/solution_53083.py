"Dadas duas strings, retorna a combinação das duas no seguinte formato: <primeira string> +"
"<segunda string> + <segunda string> + <primeira string>."
"str, str -> str"

def concatenacao(a, b):
    palavrasConcatenadas = a + b + b + a
    return palavrasConcatenadas