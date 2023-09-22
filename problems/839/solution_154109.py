def carros(p,c=5):
    '''função retorna o número exato de carros necessários, dado  pessoas p e capacidade c.
    int, int -> int'''
    return math.ceil(p/c)