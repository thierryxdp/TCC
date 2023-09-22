#
#
#
#
def primo(n):
    i=2
    while i<=round(n/2):
        if not n%i==0:
            i=i+1
        return True        
    return False