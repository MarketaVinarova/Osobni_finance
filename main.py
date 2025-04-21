from income_expenses import Record
from datetime import datetime

record = Record(kind=1, price=12, date=datetime(year=2025,month=4,day=14), items_list="4x rohlík", category="potraviny",where="Albert")
record.new_file_with_header()
record.add_record_to_file()

record2 = Record(kind=1, price=53, date=datetime(year=2025,month=4,day=15), items_list="toaletní papír", category="drogerie",where="DM")
record2.add_record_to_file()