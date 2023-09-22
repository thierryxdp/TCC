def pontos_por_time (cv, ce, cs, fv, fe, fs):
    """ugghgj"""
    golmengo = (3*cv) + ce
    golmintias= (3*fv) + fe
    if golmengo > golmintias:
        return 'Cormengo'
    if golmengo < golmintias:
        return 'Flaminthians'
    if golmengo == golmintias and cs > fs:
        return 'Cormengo'
    elif golmengo == golmintias and fs > cs:
         return 'Flaminthians'
    elif golmengo == golmintias and cs == fs:
         return 'Empate'