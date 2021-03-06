from typing import Callable
from typing import List

import pytest

from py_algorithms.dynamic_connectivity import dynamic_connectivity_brute_force
from py_algorithms.dynamic_connectivity import dynamic_connectivity_quick_union
from py_algorithms.dynamic_connectivity import dynamic_connectivity_weighted_quick_union
from py_algorithms.dynamic_connectivity import dynamic_connectivity_weighted_quick_union_pc
from py_algorithms.dynamic_connectivity import DynamicConnectivity


@pytest.fixture
def payload() -> List[int]:
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def helper_impl(f: Callable[[List[int]], DynamicConnectivity]) -> None:
    impl = f(payload())
    assert impl.is_connected(0, 9) is False
    impl.connect(0, 9)
    assert impl.is_connected(0, 9) is True

    assert impl.is_connected(0, 1) is False
    impl.connect(0, 1)
    assert impl.is_connected(0, 9) is True

    assert impl.is_connected(5, 8) is False
    impl.connect(5, 8)
    assert impl.is_connected(5, 8) is True

    assert impl.is_connected(9, 8) is False
    impl.connect(9, 8)
    assert impl.is_connected(9, 8) is True

    # Transitivity rule
    assert impl.is_connected(5, 9) is True


class TestDynamicConnectivity:
    def test_brute_force(self):
        helper_impl(dynamic_connectivity_brute_force)

    def test_quick_union(self):
        helper_impl(dynamic_connectivity_quick_union)

    def test_weighted_quick_union(self):
        helper_impl(dynamic_connectivity_weighted_quick_union)

    def test_weighted_quick_union_pc(self):
        helper_impl(dynamic_connectivity_weighted_quick_union_pc)
