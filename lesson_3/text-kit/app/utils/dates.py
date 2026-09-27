from datetime import date


def parse_date(text: str) -> date:
    day, month, year = (int(part) for part in text.split("."))
    return date(year, month, day)


def format_date(value: date) -> str:
    return f"{value.day:02d}.{value.month:02d}.{value.year}"


def is_weekend(value: date) -> bool:
    return value.weekday() >= 5


def days_between(first: date, second: date) -> int:
    return abs((second - first).days)
