def total(lista,valores):
    numero=0
    for produtos in lista:
        if produtos in valores:
            numero+=valores[produtos]
    return round(numero,2)# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis