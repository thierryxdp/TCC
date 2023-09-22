def colchoes(medidas:list[int], H: int, L: int) -> bool:
    x1 = min(medidas)
    l1 = [H,L]
    t =min(l1)
    if x1 <= t:
        medidas.remove(min(medidas))
        x2 = min(medidas)
        l1.remove(min(medidas)):
            return True
        else:
            return False
    else:
        return False