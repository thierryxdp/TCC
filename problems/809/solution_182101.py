def intercala(l1,l2)
    """Fatia as listas e as organiza de forma a intercalar l1 e l2
    list + list -> list"""
    l3 = l1 + l2
    l3[::2] = l1
    l3[1::2] = l2
    return l3