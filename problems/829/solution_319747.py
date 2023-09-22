def soma_h(n):
    """Este código recebe o limite do tamanho do denominador,e realiza 
    somas com todas as frações com denominadores menores que o inserido,
    incluindo a fração com o denominador inserido, assim como diz a
    fórmula. O valor é retornado com duas casas decimais.
    Recebe: int
    Retorna: float"""
    total = []
    denominador = 1
    
    while denominador <= n:
        x = 1/denominador
        list.append(total, x)
        denominador = denominador + 1
    return round(sum(total), 2)