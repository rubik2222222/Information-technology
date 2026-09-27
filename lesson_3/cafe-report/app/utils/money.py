def to_rubles(kopeks: float) -> float:
    return round(kopeks / 100, 2)


def format_rubles(rubles: float) -> str:
    text = f"{rubles:,.2f}".replace(",", " ").replace(".", ",")
    return f"{text} ₽"
