# === Stage 3: Хранилище в памяти ===
# Project: PlantNursery
memory_store.py

import uuid
from datetime import date


class Party:
    def __init__(self, name, culture, quantity, sowing_date):
        self.id = uuid.uuid4().hex
        self.name = name
        self.culture = culture
        self.quantity = quantity
        self.sowing_date = sowing_date

    def __repr__(self):
        return f"Party(id={self.id}, name={self.name!r}, culture={self.culture!r}, quantity={self.quantity}, sowing_date={self.sowing_date!r})"


class InMemoryPartyStore:
    def __init__(self):
        self._parties = {}

    def add(self, party):
        self._parties[party.id] = party
        return party

    def get(self, party_id):
        return self._parties.get(party_id)

    def list(self):
        return list(self._parties.values())

    def count(self):
        return len(self._parties)


def main():
    store = InMemoryPartyStore()

    party1 = Party("Рассада томатов", "tomato", 500, date(2026, 2, 10))
    party2 = Party("Рассада перца", "pepper", 300, date(2026, 2, 15))
    party3 = Party("Рассада огурцов", "cucumber", 400, date(2026, 2, 20))

    store.add(party1)
    store.add(party2)
    store.add(party3)

    print(f"Всего партий: {store.count()}")

    retrieved = store.get(party1.id)
    print(f"Получили по id {party1.id[:8]}: {retrieved}")

    print("Список партий:")
    for party in store.list():
        print(f"  {party.name} ({party.culture}), {party.quantity} шт., посев {party.sowing_date}")


if __name__ == "__main__":
    main()
