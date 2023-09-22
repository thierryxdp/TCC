#
#
#
#
def primo(n):
    i=2
    while i<=(n/2):
        if not n%i==0:
        i=i+1
        return False        
    return True