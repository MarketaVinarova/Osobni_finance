import pandas as pd
from datetime import datetime

class Record:
    # Vlastnosti:
    #   kind = typ: 1 = výdaj, 2 = příjem, 3 = půjčím si, 4 = vrátím půjčku, 5 = půjčím někomu, 6 = vrátí se mi
    #   price = celková cena za 1 výdaj nebo 1 příjem, např. celková cena za 10 položek na účtence v 1 obchodě
    #   date = datum, kdy bylo nakoupeno nebo kdy přišly peníze
    #   items_list = seznam, co bylo nakoupeno, např. "rohlíky, mléko, jogurt"
    #   category = kategorie, např. jídlo, drogerie, cestování,...
    #   where = kde jsem nakoupila, komu jsem půjčila, od koho je příjem,...
    def __init__(self, kind: int, date: datetime, price: float, items_list: str, category: str, where: str) -> None:
        self.kind = kind
        self.price = price
        self.date = date
        self.items_list = items_list
        self.category = category
        self.where = where

    def read_record_from_file(self) -> None:
        pass
        # try:
        #     list_of_records_df = pd.read_csv("list_of_records.csv")
        #     with open("list_of_records.csv", "r") as file:
        #         result = file.read()
        # except FileNotFoundError as e:
        #     print("File wasn´t found.")

    @staticmethod
    def file_exists(path: str) -> bool:
        try:
            with open(path, "r") as file:
                return True
        except FileNotFoundError:
            return False

    @staticmethod
    def new_file_with_header(path: str) -> None:
        try:
            df = pd.DataFrame(
                {"typ": [],
                 "date": [],
                 "cena": [],
                 "za co": [],
                 "category": [],
                 "kde": []}
            )
            df.to_csv(path_or_buf=path, mode="w", index=False, sep=";", header=True)

        except Exception as e:
             print("Chyba práce se souborem.")

    def add_record_to_file(self, path: str) -> None:
        try:
            df = pd.DataFrame(
                {"typ": [self.kind],
                 "date": [self.date],
                 "cena": [self.price],
                 "za co": [self.items_list],
                "category": [self.category],
                 "kde": [self.where]}
            )

            df.to_csv(path_or_buf=path, mode="a", index=False, sep=";", header=False)

        except FileNotFoundError as e:
            print("File wasn´t found.")

    def print_record(self) -> str:
        ...