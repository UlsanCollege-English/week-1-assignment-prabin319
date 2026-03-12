"""
Week 1 — Intro Challenges

Rules:
- Implement the functions below.
- Do NOT change function names or parameters (tests depend on them).
- Keep solutions readable and simple.
- Stdlib only.

Tip:
Run tests from repo root:
    pytest -q
"""

from __future__ import annotations
from collections.abc import Iterable, Sequence
from typing import Optional, TypeVar

T = TypeVar("T")

def add(a: int, b: int) -> int:
    return a + b

def is_even(n: int) -> bool:
    return n % 2 == 0

def linear_search(nums: Sequence[T], target: T) -> Optional[int]:
    for i, val in enumerate(nums):
        if val == target:
            return i
    return None

def count_occurrences(items: Iterable[T], target: T) -> int:
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count

def last_index(nums: Sequence[T], target: T) -> Optional[int]:
    result = None
    for i, val in enumerate(nums):
        if val == target:
            result = i
    return result