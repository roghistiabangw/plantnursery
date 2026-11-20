# === Stage 7: Поиск дубликатов ===
# Project: PlantNursery
from datetime import date


def normalize_title(title: str) -> str:
    return " ".join(title.split()).strip().lower()


def normalize_culture(culture: str) -> str:
    return " ".join(culture.split()).strip().lower()


def normalize_quantity(quantity) -> int:
    try:
        return int(quantity)
    except (TypeError, ValueError):
        return -1


def normalize_seed_date(seed_date) -> str:
    if isinstance(seed_date, date):
        return seed_date.isoformat()
    text = str(seed_date).strip()
    if not text:
        return ""
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m/%d/%Y"):
        try:
            parsed = date.fromformat(text, fmt)
            return parsed.isoformat()
        except ValueError:
            continue
    return text


def normalize_batch(batch: dict) -> tuple:
    return (
        normalize_title(batch.get("название")),
        normalize_culture(batch.get("культура")),
        normalize_quantity(batch.get("количество")),
        normalize_seed_date(batch.get("дата посева")),
    )


def find_duplicate_batches(batches: list) -> list:
    seen = {}
    duplicates = []
    for batch in batches:
        key = normalize_batch(batch)
        if key in seen:
            duplicates.append((seen[key], batch, key))
        else:
            seen[key] = batch
    return duplicates


def print_duplicate_report(batches: list) -> None:
    duplicates = find_duplicate_batches(batches)
    if not duplicates:
        print("Дубликатов партий не обнаружено.")
        return
    print(f"Обнаружено {len(duplicates)} пар дубликатов партий:")
    for first, second, key in duplicates:
        print(f"  {first['название']} ({first['культура']}, "
              f"кол-во={first['количество']}, дата={first['дата посева']})")
        print(f"  <-> {second['название']} ({second['культура']}, "
              f"кол-во={second['количество']}, дата={second['дата посева']})")
