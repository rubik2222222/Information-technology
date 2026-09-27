def normalize_name(name: str) -> str:
    return " ".join(part.capitalize() for part in name.split())


def pad(text: str, width: int) -> str:
    if len(text) >= width:
        return text
    return text + " " * (width - len(text))
