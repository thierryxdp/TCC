def primo(x):
    l=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    c=1
    for i in l:
        if x%i==0:
            c+=1
        if i==x:
            return True
    if c>1:
        return False
    else:
        return True