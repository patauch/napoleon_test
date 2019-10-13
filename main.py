def fast_sort(listik,pr):
    if pr == 0:
        list_3 = []
        list_not_3 = []
        for b in listik:
            if b % 3 == 0:
                list_3.append(b)
            else:
                list_not_3.append(b)
        return fast_sort(list_3, 1) + fast_sort(list_not_3, 1)
    else:
        if len(listik) > 1:
            list_less = []
            list_more = []
            list_base = []
            print(len(listik))
            base = listik[len(listik)//2]
            for j in listik:
                if j < base:
                    list_less.append(j)
                elif j > base:
                    list_more.append(j)
                else:
                    list_base.append(j)
            return fast_sort(list_less, 1)+list_base+fast_sort(list_more, 1)
        else:
            return listik

A=[]
b = 0
check = 1
while check == 1:
    N = int(input())
    stri = input().split(' ')
    if len(stri) != N:
        print("Ошибка условия")
        continue
    for i,it in enumerate(stri):
        A.append(int(it))
    print(A)
    A = fast_sort(A, 0)
    print(A)
    check = 0
