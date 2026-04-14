def slow_function(data):
    result = []
    for i in data:
        for j in data:
            if i == j:
                result.append(i)
    return result


def fast_function(data):
    return list(set(data))
