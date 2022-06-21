# 리모컨
channel = int(input())
n_broken = int(input())
n = list(map(int,input().split()))
use = []
l = []
cnt = 0
for i in range(0,10):
    if i not in n:
        use.append(i)
    else:
        pass
        
# def checking(number):
chk = str(channel)

for i in range(len(chk)):
    # 고장나지 않은 번호인 경우 단순히 버튼을 한개만 누름 되기 때문에 1 추가
    if int(chk[i]) in use:
        cnt += 1 
    
    # 고장난 번호인 경우 상황인 경우 상황이 복잡해진다. 먼저 자릿수를 생각하여 l에 더해준다.
    else:
        for j in range(len(use)):
            # 체킹을 위한 덧셈, 자릿수만큼 채널을 옮기는 횟수를 생각해주었다.
            l.append(number // (10 ** (len(chk)-(i+1))) - use[j])
            print(l)
            # 음수인 경우는 삭제.. 여기서부터 조금 꼬여가는 듯 했다.
            if l[-1] < 0:
                del l[-1]
            # 너무 변수를 많이 사용해져 다시 코드를 보았더니 이해가 잘되지 않는 포인트
            number = number % (10 ** (len(chk)-(i+1))
        cnt += min(l) * (10 ** (chk_len-1))
        l = []
print(cnt)
                               
#자릿수 비교하면서 별 깽판은 다쳤지만 실패

# 정답풀이
channel = int(input())
abs_chn = abs(100 - channel) 
n_broken = int(input())
if n_broken: 
    broken = set(input().split())
else:
    broken = set()

for num in range(1000001): 
    for N in str(num):
        if N in broken:
            break
    else: 
     # min을 활용하고 반복할 수 있는 탐색 알고리즘을 사용하여 보다 깔끔하게 값을 갱신해 나갈 수 있었다.
        abs_chn = min(abs_chn, len(str(num)) + abs(num - channel))

print(abs_chn)

# 문제에 제시된 숫자의 범위를 활용할 것
# cnt값을 더하는 형식이 아닌, 갱신하는 형식에 대해 고민해보고 적절히 활용해볼 것
# 구체적으로 생각해보고 때로는 멀리 바라보고 생각할 
