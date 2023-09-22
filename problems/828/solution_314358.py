def primo(n: int) -> int:
    """comentário"""
    zeros = 0
    for i in list(range(1, n+1)):
        if n % i == 0:
            zeros += 1
    if zeros == 2:
        return True
    else:
        return False