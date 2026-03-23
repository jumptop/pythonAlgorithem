N = input() # 입력받은 수
total = 0 # *을 제외한 모두를 더한 수
star_weight = 0 # *의 가중치가 1인지 3인지 판별

for i in range(13): # ISBN은 13자리이므로 13번 반복
    if N[i] == '*': # N이 *일때
        star_weight = 1 if i % 2 == 0 else 3 # 0부터 시작하는 ISBN 특성상 짝수라면 == 1 홀수라면 3을 가져와서 가중치에 더함
    else:
        weight = 1 if i % 2 == 0 else 3 # N이 *이 아닌 일반 수라면 가중치를 먼저 가져온다. 공식은 star_weight와 같음
        total += int(N[i]) * weight # 더해서 모으는 값(total)에 N[i]번째 값을 숫자로 변환시키고 가중치만큼 곱하여 저장

for m in range(10): # 10번 반복(맞는 수를 찾기 위함, 다음 공식을 따름 10 - total % 10 = *
    if (total + m * star_weight) % 10 == 0: # total에 m * star_weight(별 가중치)를 더해서 10으로 나누면 0이 되는 수가 *의 수임
        print(m) # 그 *의 수 출력
        break # 멈추기