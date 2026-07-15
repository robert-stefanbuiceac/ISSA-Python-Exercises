from Intro.main import prim

def cel_mai_mare_prim(s):
    nr=[]
    cifre=[]

    for c in s:
        if c.isdigit():
            cifre.append(c)
        else:
            if cifre:
                numar=int("".join(cifre))
                nr.append(numar)
                cifre=[]
    if cifre:
        nr.append(int("".join(cifre)))
    maxim=-1
    for numar in nr:
        if prim(numar):
            if numar>maxim:
                maxim=numar
    return maxim

print (cel_mai_mare_prim("EuLucrez"))
print (cel_mai_mare_prim("ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda"))