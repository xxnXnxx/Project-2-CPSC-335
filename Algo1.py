def wait_times(house_candies):
    n = len(house_candies)
    wait_times = [0] * n
    stack = []  # Store indices of houses with decreasing candy amounts

    for i in range(n - 1, -1, -1):
        while stack and house_candies[stack[-1]] <= house_candies[i]:
            stack.pop()

        if stack:
            wait_times[i] = stack[-1] - i
        stack.append(i)

    return wait_times

# Example usage:
house_candies = [3, 5, 8, 2, 1, 4, 10, 6]
result = wait_times(house_candies)
print(result)  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
