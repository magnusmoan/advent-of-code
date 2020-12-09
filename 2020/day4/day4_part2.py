from pathlib import PosixPath
import re
from typing import Dict

file_path = PosixPath(".") / "day4.txt"
data = file_path.read_text().split("\n\n")
passports = []

for passport in data:
    curr = list(filter(len, passport.replace("\n", " ").split(" ")))
    passport_dict = {}
    for item in curr:
        passport_dict[item.split(":")[0]] = item.split(":")[1]
    passports.append(passport_dict)


def valid_number(digits, least, most, data):
    if digits and len(data.strip()) != digits:
        return False

    try:
        number = int(data)
    except ValueError:
        return False
    
    return least <= number <= most


def valid_height(data):
    if "in" in data:
        loc = data.index("in")
        if loc != len(data) - 2:
            return False
        return valid_number(2, 59, 76, data[:loc])
    if "cm" in data:
        loc = data.index("cm")
        if loc != len(data) - 2:
            return False
        return valid_number(3, 150, 193, data[:loc])
    return False


def valid_pid(data):
    return re.search("^[0-9]{9}$", data) is not None


def valid_hair_color(data):
    return re.search("^#[0-9a-f]{6}$", data) is not None


def valid_eye_color(data):
    return data in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def is_valid(passport: Dict[str, str]) -> bool:
    for field in required_fields:
        field_str = field[0]
        if field_str not in passport or not field[1](passport[field_str]):
            return False

    return True


required_fields = [
        ("byr", lambda x: valid_number(4, 1920, 2002, x)), 
        ("iyr", lambda x: valid_number(4, 2010, 2020, x)),
        ("eyr", lambda x: valid_number(4, 2020, 2030, x)),
        ("hgt", valid_height),
        ("hcl", valid_hair_color),
        ("ecl", valid_eye_color),
        ("pid", valid_pid)]

print(len(list(filter(is_valid, passports))))
