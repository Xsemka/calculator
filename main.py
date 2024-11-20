def str_to_list(str_list):
    out_list = []
    c = ""
    for i in str_list:
        for j in i:
            if j in "123456789":
                c += j
            elif j == "," or j == "]":
                out_list.append(float(c))
                c = ""
    return out_list

def right_type(a):
    for i in range(len(a)):
        try:
            a[i] = int(a[i])
        except:
            pass
    return a


def calcult(a):
    for i in range(0, len(a)-1):
        if a[i] == "*":
            if type(a[i-1]) == type(a[i+1]):
                a[i] = a[i-1] * a[i+1]
                a.pop(i+1)
                a.pop(i-1)
            elif isinstance(a[i-1], list):
                a[i] = list(map(lambda x: x * a[i+1], a[i-1]))
                a.pop(i+1)
                a.pop(i-1)
            elif isinstance(a[i+1], list):
                a[i] = list(map(lambda x: x * a[i-1], a[i+1]))
                a.pop(i+1)
                a.pop(i-1)

        elif a[i] == "/":
            if type(a[i-1]) == type(a[i+1]):
                a[i] = a[i-1] / a[i+1]
                a.pop(i+1)
                a.pop(i-1)
            elif isinstance(a[i-1], list):
                a[i] = list(map(lambda x: x / a[i+1], a[i-1]))
                a.pop(i+1)
                a.pop(i-1)
            elif isinstance(a[i+1], list):
                a[i] = list(map(lambda x: a[i-1] / x, a[i+1]))
                a.pop(i+1)
                a.pop(i-1)

        elif a[i] == "+":
            if type(a[i-1]) == type(a[i+1]):
                a[i] = a[i-1] + a[i+1]
                a.pop(i+1)
                a.pop(i-1)
            elif isinstance(a[i-1], list):
                a[i] = list(map(lambda x: x + a[i+1], a[i-1]))
                a.pop(i+1)
                a.pop(i-1)
            elif isinstance(a[i+1], list):
                a[i] = list(map(lambda x: x + a[i-1], a[i+1]))
                a.pop(i+1)
                a.pop(i-1)

        elif a[i] == "-":
            if type(a[i-1]) == type(a[i+1]):
                a[i] = a[i-1] - a[i+1]
                a.pop(i+1)
                a.pop(i-1)
            elif isinstance(a[i-1], list):
                a[i] = list(map(lambda x: x - a[i+1], a[i-1]))
                a.pop(i+1)
                a.pop(i-1)
            elif isinstance(a[i+1], list):
                a[i] = list(map(lambda x: a[i-1] - x, a[i+1]))
                a.pop(i+1)
                a.pop(i-1)

    return a


a = input().split()
print(calcult(right_type(list(map(lambda x:str_to_list(x) if x[0] == "[" else x, a)))))

