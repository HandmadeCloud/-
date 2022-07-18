def is_palindrome(num):
    if str(num) != str(num)[::-1]:
        return False
    return num

def is_prime(num):
    if num == 1:
        return False
    for i in range(2,num-1):
        if num % i == 0:
            return False
    return num


n = int(input())

while True:
    if is_palindrome(n) == False:
        n += 1
    else: 
        if is_prime(n) == False:
            n += 1
        else:
            print(n)
            break
