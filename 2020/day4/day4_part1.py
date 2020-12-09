from pathlib import PosixPath

file_path = PosixPath(".") / "day4.txt"
data = file_path.read_text().split("\n\n")

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def is_valid(passport: str) -> bool:
    for field in required_fields:
        if f"{field}:" not in passport:
            return False
    
    return True


print(len(list(filter(is_valid, data))))
