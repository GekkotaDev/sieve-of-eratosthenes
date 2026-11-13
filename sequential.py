import dataclasses
import enum

import rich
from beartype import beartype
from rich.prompt import IntPrompt

SIEVE_OFFSET = 2


class Status(enum.Enum):
    COMPOSITE = enum.auto()
    PRIME = enum.auto()


@dataclasses.dataclass
class Indice:
    number: int
    status: Status = Status.PRIME


@beartype
def compute_multiples(n: int, limit: int) -> set[int]:
    multiples = set[int]()
    counter = n + n

    while counter <= limit:
        multiples.add(counter)
        counter = counter + n
    return multiples


def main():
    limit = IntPrompt.ask("n?")
    interval = range(2, limit + 1)
    sieve = [Indice(index) for index in interval]

    sieve[0].status = Status.PRIME

    for n in sieve:
        if n.status == Status.COMPOSITE:
            continue

        for multiple in compute_multiples(n.number, limit):
            sieve[multiple - SIEVE_OFFSET].status = Status.COMPOSITE

    primes = filter(lambda n: n.status == Status.PRIME, sieve)
    rich.print([*primes])


if __name__ == "__main__":
    main()
