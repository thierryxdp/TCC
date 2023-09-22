def qtd_divisores(x):
    r = 0
    for a in list(range(x+1))[1::]:
        if x%a == 0:
            r += 1
    return r


def primo(x):
    r = 0
    if x%2 == 0:
        return False
    else:
        for a in list(range(x)[3:-1:2]:
                      if x%a == 0:
                      r += 1
              return r == 0