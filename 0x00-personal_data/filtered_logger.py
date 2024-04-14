#!/usr/bin/env python3
"""Filtering module
"""

import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


"""
Main file
"""

# fields = ["password", "date_of_birth"]
# messages = [
#    "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
#    "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]
#
# for message in messages:
#    print(filter_datum(fields, 'xxx', message, ';'))
