# === Stage 5: Генерация идентификаторов ===
# Project: PlantNursery
import string
import secrets


PROJECT_PREFIX = "PN"


def generate_unique_id(prefix: str) -> str:
    """Генерация уникального идентификатора с проверкой коллизий.

    Формат: префикс + разделитель + 10 символов из набора
    прописных букв и цифр (base36). Вернуть можно только после
    проверки на отсутствие дубликатов среди уже сгенерированных.
    """
    alphabet = string.ascii_uppercase + string.digits
    while True:
        candidate = f"{prefix}-{secrets.token_hex(4).upper()}"
        if candidate not in used_ids:
            used_ids.add(candidate)
            return candidate


used_ids: set[str] = set()


def main() -> None:
    ids = [generate_unique_id(PROJECT_PREFIX) for _ in range(5)]
    print(ids)


if __name__ == "__main__":
    main()
