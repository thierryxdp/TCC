def primo(n: int) -> bool:
    for i in range(n):
        if n%(i+1) == 0:
            return false
        else:
            return true