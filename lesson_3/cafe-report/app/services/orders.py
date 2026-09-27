import csv
from pathlib import Path

from app.utils.text import normalize_name


def load_orders(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return [
            {"waiter": normalize_name(row["waiter"]), "kopeks": int(row["kopeks"])}
            for row in reader
        ]


def total_kopeks(orders: list[dict]) -> int:
    return sum(order["kopeks"] for order in orders)


def average_kopeks(orders: list[dict]) -> float:
    if not orders:
        raise ValueError("Список заказов пуст")
    return total_kopeks(orders) / len(orders)


def kopeks_by_waiter(orders: list[dict]) -> dict:
    result: dict = {}
    for order in orders:
        waiter = order["waiter"]
        result[waiter] = result.get(waiter, 0) + order["kopeks"]
    return result
