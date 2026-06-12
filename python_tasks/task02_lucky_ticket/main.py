def can_make_lucky_ticket(digits: tuple[int, int, int, int, int, int]) -> bool:
    return sum(digits[:3]) == sum(digits[3:])


if __name__ == "__main__":
    example = (1, 2, 3, 3, 2, 1)
    print(can_make_lucky_ticket(example))
