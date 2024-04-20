from openpyxl import load_workbook


def save_to_excel(path: str, data: list) -> None:
    workbook = load_workbook(filename=path)
    worksheet = workbook.active
    for row in data:
        worksheet.append(row)
    workbook.save(path)
