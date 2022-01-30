from typing import Callable, List

ProduceFn = Callable[[int], str]

def combine_strs(inputs: List[str]) -> str:
    return ''.join(inputs)

def divisible_by(k: int, n: int) -> bool:
    return n % k == 0

def produce_if_divisible_by_fn(output: str, k: int) -> ProduceFn:
    return lambda n : output if divisible_by(k, n) else ''

def combine_produce_fns(fns: List[ProduceFn]) -> ProduceFn:
    return lambda n : combine_strs([fn(n) for fn in fns]) or f'{n}'

fizzbuzz: ProduceFn = combine_produce_fns([
    produce_if_divisible_by_fn('Fizz', 3),
    produce_if_divisible_by_fn('Buzz', 5),
])
