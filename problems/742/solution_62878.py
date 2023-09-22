# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """l,slf
    Entrada: String, Int, Int
    Saída: String"""
    novastr1 = len(s)//2
    novastr2 = s[:novastr1]
    novastr3 = s[novastr1:]
    return novastr2 + x + novastr3