# A list of messy, complete street addresses and the expected,
# coarsened equivalents. Your task is to complete the function
# `coarsen` so that it produces the second string from the
# first using only bitwise operations, and the built-in
# functions `ord` and `chr`.
addrs = [
    ("119 Reed St", "000 Reed St"),
    ("253 Rindge St", "000 Rindge St"),
    ("6 Emmons Pl", "0 Emmons Pl"),
    ("   113 Walker St", "000 Walker St"),
    ("109 Walker St      ", "000 Walker St"),
    (" 30 Clay St  ", "00 Clay St"),
    ("\t  40 Montgomery St", "00 Montgomery St"),
]


def _is_trim_whitespace(code):
    """True for ASCII whitespace commonly handled by strip()."""
    return (
        (code == 32)  # space
        | (code == 9)  # tab
        | (code == 10)  # \n
        | (code == 11)  # \v
        | (code == 12)  # \f
        | (code == 13)  # \r
    )


def coarsen(full_addr):
    """Given a messy full street address return a clean coarsened one."""
    start = 0
    end = len(full_addr) - 1

    while (start <= end) & _is_trim_whitespace(ord(full_addr[start])):
        start += 1
    while (end >= start) & _is_trim_whitespace(ord(full_addr[end])):
        end -= 1

    coarsened_chars = []
    for i in range(start, end + 1):
        code = ord(full_addr[i])
        is_digit = ((code & 0b11110000) == 0b00110000) & (
            (code & 0b00001111) <= 9
        )
        if is_digit:
            coarsened_chars.append(chr(code & 0b11110000))
        else:
            coarsened_chars.append(chr(code))

    return "".join(coarsened_chars)


def main():
    """Driver that tests your function."""
    for full_addr, coarsened_addr in addrs:
        r = coarsen(full_addr)
        if r == coarsened_addr:
            print(f'PASSED on test: "{full_addr}"')
        else:
            print(f'FAILED on "{full_addr}", returned:\n\t"{r}"')


if __name__ == "__main__":
    main()
