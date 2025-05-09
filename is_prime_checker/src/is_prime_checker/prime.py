def is_prime(number):
    count = 0

    if number <= 1:
        return False

    for i in range(1, number+1):
        if number % i == 0:
            count += 1
            
    return count == 2

