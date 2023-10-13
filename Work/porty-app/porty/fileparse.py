# fileparse.py
#
# Exercise 3.3
import csv
import logging
from typing import Optional, Callable

logger = logging.getLogger(__name__)


def parse_csv(
    lines,
    select: Optional[list[str]] = None,
    types: Optional[list[Callable]] = None,
    has_headers: bool = True,
    delimiter=",",
    silence_errors: bool = False,
):
    """
    Parse a CSV file into a list of records
    """

    if select and not has_headers:
        raise RuntimeError("select requires column headers")

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers if any
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering
    indices = []
    if select:
        indices = [headers.index(col) for col in select]
        headers = select

    records = []
    for i, row in enumerate(rows, 1):
        if not row:
            continue

        if select:
            row = [row[index] for index in indices]

        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    logger.warning(f"Row {i}: Couldn't convert {row}")
                    logger.debug(f"Row {i}: Reason: {e}")
                continue

        # Make a dictionary or a tuple
        record = dict(zip(headers, row)) if headers else tuple(row)
        records.append(record)

    return records
