def solution(triangle):
    answer = 0
    # 2차원 배열에서 내부 배열의 총 수량까지 순회
    # DP는 작은 문제를 어떻게 설정할지가 가장 중요함 => 마지막 직전 라인의 최댓값을 구하면서 올라가자!
    # bottom up 방식 : 마지막에서 직전 줄에서 각 자리의 최댓값을 구해서 배열을 대체함 
    
    lent = len(triangle)
    for i in range(lent):
        idx = lent - i - 1
        
        if(i == 0): 
            continue
        
        for idx2, j in enumerate(triangle[idx]):
            triangle[idx][idx2]=(max(j+triangle[idx+1][idx2], j+triangle[idx+1][idx2+1]))
            
        
    return triangle[0][0]
