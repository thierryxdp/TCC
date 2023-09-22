def bolos(t,o,s):
    """calcula a quantidades de bolos qeu se pode fazer com base nos ingredientes disponiveis"""
    return int(min(t/2,o/3,s/5))