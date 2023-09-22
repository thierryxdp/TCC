# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    """retorna a concatenação das duas strings no formato abba;
    assinatura: str,str--> str
    teste:
    concatenacao('pintalgar', '')=='pintalgarpintalgar'
    concatenacao('cirzo', 'Mark')== 'cirzoMarkMarkcirzo'
    concatenacao('alcatraz', 'gauchai')=='alcatrazgauchaigauchaialcatraz'
    """
    return a+b+b+a