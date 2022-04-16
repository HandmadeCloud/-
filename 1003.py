# 1003 피보나치
zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[num], one[num]))

T = int(input())
    
for _ in range(T):
    fibonacci(int(input()))
    
    
# 피보나치를 항상 일반적인 형식으로만 생각해봤기 때문에 접근이 쉽지 않아 결국 정답의 힘을 빌렸다..
# 테스트 케이스를 0일때, 1일때, 2일때로 리스트 화를 하여 따로 저장해두면 재귀형식의 방법을 사용하지 않아도 성공할 수 있음을 보여주더라..
# 정말 그냥 놀라울 따름의 코딩이었다. 어떻게 사람들은 이런 생각을 할까...하며 다양한 접근 방식을 한수 배워간닿ㅎ
