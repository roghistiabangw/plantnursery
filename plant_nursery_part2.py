# === Stage 2: Проверка полей ===
# Project: PlantNursery
import datetime


class Party:
    def __init__(self, name, culture, quantity, sowing_date):
        self.name = name
        self.culture = culture
        self.quantity = quantity
        self.sowing_date = sowing_date


def normalize_name(value):
    return value.strip().title()


def normalize_culture(value):
    return value.strip().lower()


def normalize_quantity(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError("Количество должно быть целым числом.")


def normalize_sowing_date(value):
    try:
        return datetime.date.fromisoformat(value.strip())
    except ValueError:
        raise ValueError("Дата посева должна быть в формате ГГГГ-ММ-ДД.")


def validate_party(name, culture, quantity, sowing_date):
    if not name or not name.strip():
        raise ValueError("Название партии не может быть пустым.")
    if not culture or not culture.strip():
        raise ValueError("Культура не может быть пустой.")
    try:
        quantity = normalize_quantity(quantity)
    except ValueError:
        raise
    if quantity <= 0:
        raise ValueError("Количество должно быть больше нуля.")
    try:
        sowing_date = normalize_sowing_date(sowing_date)
    except ValueError:
        raise
    if sowing_date > datetime.date.today():
        raise ValueError("Дата посева не может быть в будущем.")
    return Party(
        normalize_name(name),
        normalize_culture(culture),
        quantity,
        sowing_date,
    )


if __name__ == "__main__":
    try:
        party = validate_party(
            "  томатный рассадник  ",
            "Томат",
            "abc",
            "2024-13-01",
        )
        print(party)
    except ValueError as error:
        print("Ошибка:", error)
