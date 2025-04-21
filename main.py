from income_expenses import Record
from datetime import datetime

path = "list_of_records.csv"

record = Record(kind=1, price=12, date=datetime(year=2025,month=4,day=14), items_list="4x rohlík", category="potraviny",where="Albert")
file_exists = record.file_exists(path)
if not file_exists:
    record.new_file_with_header(path)
record.add_record_to_file(path)

record2 = Record(kind=1, price=53, date=datetime(year=2025,month=4,day=15), items_list="toaletní papír", category="drogerie",where="DM")
file_exists = record2.file_exists(path)
if not file_exists:
    record2.new_file_with_header(path)
record2.add_record_to_file(path)