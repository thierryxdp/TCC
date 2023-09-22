def repetidos(valores):
    valores = []
repetidos = set()

for dado in dados:
    if dado not in valores:
        valores.append(dado)
    else:
        repetidos.add(dado)
return(f'Valores = {valores}')
return(f'Repetidos = {repetidos}')