# === Stage 10: Просмотр истории ===
# Project: PlantNursery
from datetime import date


def format_party_record(party):
    """Форматирует запись партии в компактный вид."""
    name = party.get("название", "Без названия")
    culture = party.get("культура", "Без культуры")
    quantity = party.get("количество", 0)
    sowing_date = party.get("дата посева")
    date_str = sowing_date.strftime("%d.%m.%Y") if isinstance(sowing_date, date) else sowing_date

    return (
        f"Партия #{party.get('id', '?')} | {name} | {culture} | "
        f"кол-во: {quantity} | посев: {date_str}"
    )


def party_history(party):
    """Возвращает историю одной записи партии в компактном виде."""
    if not isinstance(party, dict):
        return "Неверная запись партии."

    lines = [format_party_record(party)]

    history = party.get("история", [])
    if history:
        lines.append("Этапы:")
        for step in history:
            event_type = step.get("тип", "Этап")
            event_date = step.get("дата")
            event_date_str = event_date.strftime("%d.%m.%Y") if isinstance(event_date, date) else event_date
            lines.append(f"  - {event_type}: {event_date_str}")

    return "\n".join(lines)


if __name__ == "__main__":
    sample_party = {
        "id": 101,
        "название": "Рассада томатов",
        "культура": "Помидор",
        "количество": 500,
        "дата посева": date(2024, 3, 15),
        "история": [
            {"тип": "Посев", "дата": date(2024, 3, 15)},
            {"тип": "Пикировка", "дата": date(2024, 3, 25)},
            {"тип": "Закалка", "дата": date(2024, 4, 10)},
        ],
    }
    print(party_history(sample_party))
