import math
def primo(x):
    while 2 <= math.sqrt(x):
        if x % 2 < 1:
            return False;
        else:
            True