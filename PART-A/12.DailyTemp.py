def dailyTemperatures(T):
    stack = []
    res = [0]*len(T)

    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)

    return res


print(dailyTemperatures([73,74,75,71,69,72,76,73]))