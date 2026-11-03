# === Stage 1: Каркас модуля ===
# Project: PlantNursery
import datetime


class PartyError(Exception):
    pass


@dataclass
class Party:
    name: str
    culture: str
    quantity: int
    sowing_date: datetime.date


def create_demo_parties() -> list[Party]:
    sowing_date = datetime.date(2025, 1, 15)
    return [
        Party(name="Партия А", culture="Помидор", quantity=100, sowing_date=sowing_date),
        Party(name="Партия Б", culture="Перец", quantity=50, sowing_date=sowing_date),
        Party(name="Партия В", culture="Огурец", quantity=75, sowing_date=sowing_date),
    ]


def main() -> None:
    parties = create_demo_parties()
    for party in parties:
        print(f"Партия: {party.name}, Культура: {party.culture}, "
              f"Количество: {party.quantity}, Дата посева: {party.sowing_date}")


if __name__ == "__main__":
    main()
