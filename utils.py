import re
from lots import lots


def find_lot(lot):
    """
    Поиск полного названия лота.
    Например:
    41 -> 41/400
    41/400 -> 41/400
    """

    if "/" in lot:
        return lot if lot in lots else None

    for key in lots:
        if key.startswith(lot + "/"):
            return key

    return None



def format_lot_name(lot_key):
    """
    Убираем /400 из отображения
    """

    if lot_key.endswith("/400"):
        return lot_key.replace("/400", "")

    return lot_key



def calculate_chests(text):

    lines = text.split("\n")

    data = []

    totals = []


    for line in lines:

        match = re.search(
            r'([\d/]+)\s*:\s*(\d+)',
            line
        )

        if not match:
            continue


        lot_input = match.group(1)
        count = int(match.group(2))


        lot_key = find_lot(lot_input)


        if not lot_key:
            data.append(
                {
                    "sort": 9999,
                    "text": f"❌ {lot_input} — лот не найден"
                }
            )
            continue



        chests = lots[lot_key]


        multiplied = [
            x * count for x in chests
        ]


        # создаём место под итог
        while len(totals) < len(multiplied):
            totals.append(0)


        for i, value in enumerate(multiplied):
            totals[i] += value



        # сортировка по номеру лота
        lot_number = int(
            lot_key.split("/")[0]
        )


        display_name = format_lot_name(lot_key)


        data.append(
            {
                "sort": lot_number,
                "text":
                    f"{display_name}: {count}\n"
                    f"➜ {'/'.join(map(str, multiplied))}"
            }
        )


    if not data:
        return None



    # сортируем лоты
    data.sort(
        key=lambda x: x["sort"]
    )


    result = []

    result.append("📦 Роспись\n")


    for item in data:
        result.append(
            item["text"]
        )
        result.append("")


    # итог
    if totals:

        result.append(
            "━━━━━━━━━━━━━━"
        )

        result.append(
            "\n📊 Итого\n"
        )


        for index, value in enumerate(totals):

            result.append(
                f"📦 {index + 1} сундук: {value}"
            )


    return "\n".join(result)




def calculate_numbers(text):

    numbers = re.findall(
        r'-?\d+\.?\d*',
        text
    )


    if not numbers:
        return None


    numbers = [
        float(x)
        for x in numbers
    ]


    positive = sum(
        x for x in numbers
        if x > 0
    )


    negative = sum(
        x for x in numbers
        if x < 0
    )


    total = positive + negative


    return (
        f"➕ Положительные: {positive}\n"
        f"➖ Отрицательные: {negative}\n"
        f"📊 Итого: {total}"
    )
