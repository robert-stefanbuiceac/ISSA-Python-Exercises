


def cmmdc(a,b):
    while b != 0:
        rest = a % b
        a = b
        b = rest
    return a

def cmmdc_argvar(*nr):
    rez=nr[0]
    for x in nr[1:]:
        rez=cmmdc(rez,x)
    return rez

if __name__ == '__main__':
    print(cmmdc_argvar(100,150,250,500,1000))