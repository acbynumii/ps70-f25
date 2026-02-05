# A list of messy, complete street addresses and the expected,
# coarsened equivalents. Your task is to write the function
# `coarsen` that produces the second from the first.
addrs = [
    ("119 Reed St", "1XX Reed St"),
    ("253 Rindge St", "2XX Rindge St"),
    ("6 Emmons Pl", "0XX Emmons Pl"),
    ("   113 Walker St", "1XX Walker St"),
    ("109 Walker St      ", "1XX Walker St"),
    (" 30 Clay St  ", "0XX Clay St"),
    ("\t  40 Montgomery St", "0XX Montgomery St"),
]


def coarsen(full_addr):
    '''Given a messy full street address return a clean coarsened one'''
    full_addr = full_addr.strip()
    full_addr = full_addr.split()
    if not full_addr:
        return ""
    if len(full_addr[0]) == 1:
        full_addr[0] = "0XX"
    else:
        full_addr[0] = full_addr[0][0] + "XX"
    full_addr = " ".join(full_addr)
    return full_addr


def main():
    "Driver that tests your function."

    # You can ask a Generative AI system like ChatGPT how the next
    # for-loop works, if you are curious. You should NOT ask it to
    # write `coarsen` for you.
    for full_addr, coarsened_addr in addrs:
        r = coarsen(full_addr)
        if r == coarsened_addr:
            print(f'PASSED on test: "{full_addr}"')
        else:
            print(f'FAILED on "{full_addr}", returned:\n\t"{r}"')


if __name__ == "__main__":
    main()
