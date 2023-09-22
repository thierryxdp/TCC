# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_compra, produtos):
    valor_total = 0
    contador = 0
    limite = len(lista_compra)
    
    while contador < limite:
        valor_total += produtos[lista_compra[contador]]
        contador += 1
        
    valor_total = round(valor_total,2)
    return valor_total