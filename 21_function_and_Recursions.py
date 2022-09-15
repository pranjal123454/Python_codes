# def percent(marks):
#     p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
#     return p
# marks1=[45,78,86,77]
# percentage1=percent(marks1)
# marks2=[75,98,88,78]
# percentage2=percent(marks2)
# print(percentage1,percentage2)
#recursion

def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursive(n-1)
f=factorial_recursive(5)
print(f)
