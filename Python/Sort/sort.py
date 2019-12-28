number = [5,7,9,6,3]
print(number)

def sort(num1, num2, opr="ASC"):
    if opr == "ASC":
        if num1 >= num2:
            return num1, num2
        if num1 <= num2:
            return num2, num1
    if opr == "DESC":
        if num1 <= num2:
            return num1, num2
        if num1 >= num2:
            return num2, num1

list_range = cnt = len(number)

for i in range(0, list_range-1):
    for j in range(0, cnt-1):
        number[j], number[j+1] = sort(number[j], number[j+1], opr="DESC")
    cnt -= 1

print(number)

