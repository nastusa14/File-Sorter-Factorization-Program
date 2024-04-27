import time
from multiprocessing import Pool, cpu_count

def factorize_sync(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(numbers):
    if __name__ == '__main__':
        with Pool(cpu_count()) as pool:
            results = [pool.apply_async(factorize_sync, (number,)) for number in numbers]
            return [result.get() for result in results]

if __name__ == '__main__':
    # Перевірка часу виконання синхронної версії
    start_time = time.time()
    result_sync = factorize_parallel([128, 255, 99999, 10651060])
    end_time = time.time()
    print("Час виконання синхронної версії:", end_time - start_time)

    # Перевірка часу виконання паралельної версії
    start_time = time.time()
    result_parallel = factorize_parallel([128, 255, 99999, 10651060])
    end_time = time.time()
    print("Час виконання паралельної версії:", end_time - start_time)

    # Перевірка правильності роботи
    assert result_sync == result_parallel