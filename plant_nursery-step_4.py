# === Stage 4: Связи между сущностями ===
# Project: PlantNursery
import datetime


def load_parties(path):
    parties = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.split('|')
            if len(parts) == 4:
                parties.append({
                    'id': len(parties) + 1,
                    'name': parts[0].strip(),
                    'culture': parts[1].strip(),
                    'quantity': int(parts[2].strip()),
                    'sowing_date': datetime.date.fromisoformat(parts[3].strip()),
                })
    return parties


def load_picking(path, batch_id):
    pickings = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.split('|')
            if len(parts) == 4 and parts[0].strip() == str(batch_id):
                pickings.append({
                    'id': len(pickings) + 1,
                    'batch_id': int(parts[0].strip()),
                    'destination': parts[1].strip(),
                    'count': int(parts[2].strip()),
                    'picked_date': datetime.date.fromisoformat(parts[3].strip()),
                })
    return pickings


def get_batch_pickings(batch_id, pickings):
    return [p for p in pickings if p['batch_id'] == batch_id]


def check_integrity(batch_id, parties, pickings):
    batch = next((p for p in parties if p['id'] == batch_id), None)
    if batch is None:
        return False, 'Партия не найдена'

    referenced = {p['batch_id'] for p in pickings}
    if batch_id not in referenced:
        return False, 'Партия не имеет ни одной пикировки'

    total = sum(p['count'] for p in get_batch_pickings(batch_id, pickings))
    if total != batch['quantity']:
        return False, f'Сумма пикировок ({total}) не совпадает с количеством партии ({batch["quantity"]})'

    return True, 'Целостность проверена'


if __name__ == '__main__':
    parties = load_parties('parties.txt')
    pickings = load_picking('pickings.txt', 1)
    ok, message = check_integrity(1, parties, pickings)
    print(message)
