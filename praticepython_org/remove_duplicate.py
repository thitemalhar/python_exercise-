list = [int(x) for x in input("Enter numbers to form a list: \n").split()]

def dup(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    print (sorted(new_list))
def dup2(list):
    new_list2 = (set(list))
    print (new_list2)

dup(list)
dup2(list)