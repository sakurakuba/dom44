import random


def generate_numbers(N):
    secret_nums = []
    while len(secret_nums) < N:
        x = random.randint(1, 9)
        if x not in secret_nums:
            secret_nums.append(x)
    return secret_nums


def verify_num(arr1):
    if len(arr1) != 4:
        return False

    for el in arr1:
        if not el.isdigit():
            return False

    for i in arr1:
        if int(i) < 1 or int(i) > 9:
            return False
    return True


def validate_num(origin_arr, arr2):
    bulls = 0
    cows = 0
    for j in range(len(origin_arr)):
        if origin_arr[j] == int(arr2[j]):
            bulls += 1
        elif int(arr2[j]) in origin_arr:
            cows += 1
    if bulls == len(origin_arr):
        return f"Bulls: {bulls}, Cows: {cows}. You Win!!"
    return f"Bulls: {bulls}, Cows: {cows}"

