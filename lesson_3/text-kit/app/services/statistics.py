def average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Список чисел пуст")
    return sum(numbers) / len(numbers)


def median(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Список чисел пуст")
    ordered = sorted(numbers)
    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def spread(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Список чисел пуст")
    return max(numbers) - min(numbers)


def count_values(items: list) -> dict:
    result: dict = {}
    for item in items:
        result[item] = result.get(item, 0) + 1
    return result
