def fizzbuzz(input: str) -> str:
    n, m = map(int, input.splitlines())

    if n >= m or n < 1 or m > 10000:
        raise ValueError("values don't satisfy condition 1 <= n < m <= 10000")

    output = []
    for i in range(n, m + 1):
        current_output = 'Fizz' if i % 3 == 0 else ''
        current_output += 'Buzz' if i % 5 == 0 else ''
        output.append(str(i) if current_output == '' else current_output)
    return '\n'.join(output)
