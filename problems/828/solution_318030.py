def primo(x):
    """A função retorna se o numero é primo ou não
    int --> false/true """
    r = 0
    for i in range(x):
        if x%(i+1) == 0:
            r = r + 1
	if r>2:
        return False
    elif r<i:
        return True