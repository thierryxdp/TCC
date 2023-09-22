def bolos(n_far, n_ovos, n_leite):
    far = n_far // 2
    ovos = n_ovos // 3
    leite = n_leite // 5
    return min(far, ovos, leite)