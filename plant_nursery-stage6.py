# === Stage 6: Сортировка записей ===
# Project: PlantNursery
from datetime import datetime

class Party:
    def __init__(self, name, culture, quantity, sowing_date):
        self.name = name
        self.culture = culture
        self.quantity = quantity
        self.sowing_date = sowing_date
        self.created_at = datetime.now()

    def sort_key_name(self):
        return self.name.lower()

    def sort_key_date(self):
        return self.created_at

def sort_parties_by_name(parties, descending=False):
    reverse = descending
    return sorted(parties, key=lambda p: p.sort_key_name(), reverse=reverse)

def sort_parties_by_date(parties, descending=False):
    reverse = descending
    return sorted(parties, key=lambda p: p.sort_key_date(), reverse=reverse)

def sort_parties(parties, field="name", descending=False):
    if field == "date":
        return sort_parties_by_date(parties, descending)
    return sort_parties_by_name(parties, descending)
