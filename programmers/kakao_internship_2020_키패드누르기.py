keypad = [[1,2,3],
        [4,5,6],
        [7,8,9],
        ['*',0,'#']]

def solution(numbers, hand):

    answer = ''
    l_pos = '*'
    r_pos = '#'

    for i in numbers:

        if i in [1,4,7]:
            answer += "L"
            l_pos = i

        elif i in [3,6,9]:
            answer += "R"
            r_pos = i

        else:
            l_o_r,l_pos,r_pos = left_or_right(i,hand,l_pos,r_pos)
            answer += l_o_r

    return answer



def left_or_right(num,hand,l_pos,r_pos):
    
    l_o_r = ''
    
    # 거리를 비교할 수 있는 어떤 함수가 필요하다.
    for i in range(4):
        for j in range(3):
            if l_pos == keypad[i][j]:
                l_pos_idx = [i,j]
                

            if r_pos == keypad[i][j]:
                r_pos_idx = [i,j]

            if num == keypad[i][j]:
                obj = [i,j]

                
    l_cnt = abs(l_pos_idx[0]-obj[0]) + abs(l_pos_idx[1]-obj[1])
    r_cnt = abs(r_pos_idx[0]-obj[0]) + abs(r_pos_idx[1]-obj[1])
    

    # r 이 더 가까움
    if l_cnt > r_cnt:
        l_o_r = 'R'
        r_pos = num
        
    # l 이 더 가까움
    elif l_cnt < r_cnt:
        l_o_r = 'L'
        l_pos = num

    #둘의 거리가 같은 경우
    elif l_cnt == r_cnt:
        if hand=="left":
            l_o_r = 'L'
            l_pos = num
        else:
            l_o_r = 'R'
            r_pos = num

    return l_o_r,l_pos,r_pos
