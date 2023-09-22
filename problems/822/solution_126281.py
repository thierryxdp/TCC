def repetidos(n):
    m = 0
    m2 = -1
    final = 0
    while m<len(n):
        if n[m] == n[m2]:
            final = final + 1
            m = m + 1
            m2 = m2 + 1
        else:
            m = m + 1
            m2 = m2 + 1

    return final