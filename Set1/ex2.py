
def vocale(s):
    vocale='aeiouAEIOU'
    cnt=0
    for c in s:
        if c in vocale:
           cnt+=1
    return cnt



if __name__ == '__main__':
    s='Exercitiu pentru test vocale'
    print("Textul <<",s, ">> are ", vocale(s)," vocale")