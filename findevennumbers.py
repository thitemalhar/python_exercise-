a = [int(x) for x in input().split()]
print (a)
b = []
def even_numbers(a):
    for i in a:
        if i % 2 == 0:
            b.append(i)
    return (b)
print (even_numbers(a))