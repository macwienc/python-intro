import re
from datetime import datetime

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None


def calculate_rectangle_area(width: float, height: float) -> float:
    if not all(isinstance(x, (int, float)) for x in [width, height]):
        raise TypeError("Wymiary muszą być liczbami.")
    if width < 0 or height < 0:
        raise ValueError("Wymiary nie mogą być ujemne.")
    return width * height


def filter_even_numbers(numbers: list[int]) -> list[int]:
    if not all(isinstance(n, int) for n in numbers):
        raise TypeError("Wszystkie elementy muszą być liczbami całkowitymi.")
    return [n for n in numbers if n % 2 == 0]


def convert_date_format(date_str: str, current_format: str, target_format: str) -> str:
    try:
        parsed_date = datetime.strptime(date_str, current_format)
        return parsed_date.strftime(target_format)
    except Exception as e:
        raise ValueError(f"Niepoprawna data lub format: {e}")


def is_palindrome(text: str) -> bool:
    if not isinstance(text, str):
        return False
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]
