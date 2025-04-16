from datetime import datetime

class Record:
    # Vlastnosti:
    #   kind = typ: 1 = výdaj, 2 = příjem, 3 = půjčím si, 4 = vrátím půjčku, 5 = půjčím někomu, 6 = vrátí se mi
    #   price = celková cena za 1 výdaj nebo 1 příjem, např. celková cena za 10 položek na účtence v 1 obchodě
    #   date = datum, kdy bylo nakoupeno nebo kdy přišly peníze
    #   items_list = seznam, co bylo nakoupeno, např. "rohlíky, mléko, jogurt"
    #   category = kategorie, např. jídlo, drogerie, cestování,...
    #   where = kde jsem nakoupila, komu jsem půjčila, od koho je příjem,...
    def __init__(self, kind: int, price: float, date: datetime, items_list: str, category: str, where: str) -> None:
        self.kind = kind
        self.price = price
        self.date = date
        self.items_list = items_list
        self.category = category
        self.where = where

    def read_record_from_file(self) -> None:
        ...

    def save_record_to_file(self) -> None:
        ...

    def print_record(self) -> str:
        ...