# === Stage 9: Статусы записей ===
# Project: PlantNursery
"""
Модуль PlantNursery: статусы жизненного цикла партии и допустимые переходы.

Определяет строковые константы, представляющие стадии развития партии
рассады, а также функцию проверки допустимости перехода между ними.

Этап 9 из 52.
"""


# Статусы жизненного цикла партии рассады.
SEEDING = "seeding"          # партия создана, семена высеяны
GERMINATING = "germinating"  # всходы появились, ждём пикировки
PIKKED = "piked"             # рассада пикирована
HARDENED = "hardened"        # рассада закалена
PLANTED = "planted"          # рассада высажена в грунт


# Матрица допустимых переходов между статусами.
# Ключ — текущий статус, значение — множество допустимых следующих.
ALLOWED_TRANSITIONS = {
    SEEDING: {GERMINATING},
    GERMINATING: {PIKKED},
    PIKKED: {HARDENED},
    HARDENED: {PLANTED},
    PLANTED: set(),
}


def can_transition(from_status: str, to_status: str) -> bool:
    """Проверка допустимости перехода партии из одного статуса в другой.

    Возвращает True, если переход разрешён, иначе False.
    Переходы к текущему статусу и переходы из неизвестного статуса
    считаются недопустимыми.
    """
    if from_status not in ALLOWED_TRANSITIONS:
        return False
    return to_status in ALLOWED_TRANSITIONS[from_status]


def current_stage(stage: int) -> str:
    """Возвращает название статуса по индексу этапа (0..4)."""
    stages = [SEEDING, GERMINATING, PIKKED, HARDENED, PLANTED]
    if 0 <= stage < len(stages):
        return stages[stage]
    return None
