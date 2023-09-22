def pontos_por_time(t):
    """it returns a dictionary composed by two teams, the keys, and the team1' and team2's points in this phase"""
    return {t[0][0]: points_team(t,t[0][0]),
            t[0][1]: points_team(t,t[0][1])}
def points_team(t,s):
    p=0
    if s==t[0][0]:
        if t[0][2][0]==t[0][2][1]:
            p=1
        if t[0][2][0]>t[0][2][1]:
            p=3
        if t[1][2][1]==t[1][2][0]:
            p=p+1
        if t[1][2][1]>t[1][2][0]:
            p=p+3
        return p
    elif not s==t[0][0]:
        if t[0][2][0]==t[0][2][1]:
            p=1
        if t[0][2][1]>t[0][2][0]:
            p=3
        if t[1][2][1]==t[1][2][0]:
            p=p+1
        if t[1][2][0]>t[1][2][1]:
            p=p+3