from typing import Sequence


class FormatError(Exception):
    pass


class TableFormatter:
    def headings(self, headers: Sequence):
        """
        Emit the table headings
        """
        raise NotImplementedError

    def row(self, rowdata: Sequence):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError


class TextTableFormatter(TableFormatter):
    """
    Output portfolio in plain-text format
    """

    def headings(self, headers: Sequence):
        [print(f"{h:>10}", end=" ") for h in headers]
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rows):
        [print(f"{d:>10}", end=" ") for d in rows]
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio in CSV format
    """

    def headings(self, headers: Sequence):
        print(",".join(headers))

    def row(self, rows):
        print(",".join(rows))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio in HTML format
    """

    def headings(self, headers: Sequence):
        print("<tr>", end="")
        [print(f"<th>{h}</th>", end="") for h in headers]
        print("</tr>")

    def row(self, row):
        print("<tr>", end="")
        [print(f"<td>{r}</td>", end="") for r in row]
        print("</tr>")


def create_formatter(fmt: str = "txt"):
    match fmt:
        case "txt":
            return TextTableFormatter()
        case "csv":
            return CSVTableFormatter()
        case "html":
            return HTMLTableFormatter()
        case _:
            raise FormatError(f"Unknown format {fmt}")


def print_table(
    portfolio,
    columns: list[str] = ["name", "shares", "price"],
    formatter: TableFormatter = TextTableFormatter(),
):
    formatter.headings(columns)
    for stock in portfolio:
        formatter.row([getattr(stock, col) for col in columns])
