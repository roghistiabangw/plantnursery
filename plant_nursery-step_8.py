# === Stage 8: Массовое обновление ===
# Project: PlantNursery
import datetime

PARTY_NAME = "партия"
CULTURE = "культура"
QUANTITY = "количество"
SOWING_DATE = "дата посева"

PREVIEW = "Предварительный просмотр изменений"
CONFIRM = "Подтвердить массовое обновление"
CANCEL = "Отмена"
UPDATED = "Партий обновлено: {count}"
NO_MATCH = "Партий не найдено"
FIELD_UPDATED = "Обновлено поле {field} в партии {name}"


class PartyCollection:
    def __init__(self):
        self.parties = []

    def add_party(self, name, culture, quantity, sowing_date):
        party = {
            PARTY_NAME: name,
            CULTURE: culture,
            QUANTITY: quantity,
            SOWING_DATE: sowing_date,
        }
        self.parties.append(party)
        return party

    def find_parties(self, predicate):
        return [p for p in self.parties if predicate(p)]


def build_condition():
    """Сбор условия массового обновления из полей партии."""
    print("Условие отбора партий")
    print("(введите '0' для 'любое значение')")
    field = input(f"Поле [{PARTY_NAME}]: ").strip().lower()
    if not field:
        field = PARTY_NAME
    value = input(f"Значение для поля {field}: ").strip()
    return field, value


def compile_predicate(field, value):
    def match(party):
        current = party.get(field)
        if value == "0":
            return True
        return str(current) == value
    return match


def build_preview(collection, predicate):
    selected = collection.find_parties(predicate)
    print()
    print(PREVIEW)
    print("-" * 40)
    if not selected:
        print(NO_MATCH)
        return None
    for party in selected:
        print(f"  {party[PARTY_NAME]} | {party[CULTURE]} | "
              f"{party[QUANTITY]} | {party[SOWING_DATE]}")
    print("-" * 40)
    return selected


def apply_update(collection, selected, field, new_value):
    for party in selected:
        old = party.get(field)
        party[field] = new_value
        print(FIELD_UPDATED.format(field=field, name=party[PARTY_NAME]))
    print()
    print(UPDATED.format(count=len(selected)))


def main():
    collection = PartyCollection()
    collection.add_party("Партия А", "томат", 100, datetime.date(2024, 1, 10))
    collection.add_party("Партия Б", "перец", 50, datetime.date(2024, 1, 12))
    collection.add_party("Партия В", "огурец", 200, datetime.date(2024, 1, 15))

    field, value = build_condition()
    predicate = compile_predicate(field, value)
