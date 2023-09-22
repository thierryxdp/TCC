def bolos(a,b,c):
    '''calcula a quantidade máxima de bolos que consegue fazer dados três números inteiros A, B e C
    sendo respectivamente o número de xícaras de farinha de trigo, número de ovos e número de colheres de sopa de leite que tem em casa'''
    return min(a//2,b//3,c//5)