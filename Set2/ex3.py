from Set1.ex1 import cmmdc_argvar
def drepte_unice(puncte:list)->list:
    drepte_unice=set()
    n=len(puncte)
    if n<2:
        return []
    for i in range(n):
        for j in range(i+1,n):
            x1,y1=puncte[i]
            x2,y2=puncte[j]

            if x1==x2 and y1==y2:
                continue
            a=y1-y2
            b=x2-x1
            c=x1*y2-y1*x2

            numitor_comun=cmmdc_argvar(a,b,c)
            if numitor_comun:
                a//=numitor_comun
                b//=numitor_comun
                c//=numitor_comun
            if a < 0 or (a == 0 and b < 0):
                a, b, c = -a, -b, -c
            drepte_unice.add((a, b, c))

    return list(drepte_unice)

puncte_test = [(0, 0), (1, 1), (2, 2), (0, 2)]
rezultat = drepte_unice(puncte_test)
for dreapta in rezultat:
        a, b, c = dreapta
        print(f"{a}x + ({b})y + ({c}) = 0")