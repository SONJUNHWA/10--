import random
def lotto_numbers():
    results = []
    while len(results) < 6:
        ran_num = random.randint(1, 45)
        if ran_num not in results:
            results.append(ran_num)

    results.sort()
    return results

nubmer = lotto_numbers()
print(f"생성된 로또 번호는 {nubmer} 입니다.")