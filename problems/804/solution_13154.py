#Start your python function here
def filtra_pares(s):
    s = s[:len(s) // 2] + s[len(s) // 2:]
    if len(s) // 2 == 0:
        return s
    else: