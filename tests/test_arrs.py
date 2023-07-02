from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1) == 2
    assert arrs.get([1, 2, 3], 5, "test") == "test"
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([], -1) is None
    assert arrs.get([1, 2, 3], -1, "default") == "default"
    assert arrs.get([1, 2, 3], 3, "default") == "default"
    assert arrs.get([1, 2, 3], 2) == 3


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 0, 2) == [1, 2]
    assert arrs.my_slice([1, 2, 3], 0, 5) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -2) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -2, -1) == [2]
    assert arrs.my_slice([], 0, 2) == []
    assert arrs.my_slice([1, 2, 3], 1, 1) == []

    assert arrs.my_slice([1, 2, 3], 1, 0) == []  # Добавлен тест для проверки обратного среза
    assert arrs.my_slice([1, 2, 3], 0, -1) == [1, 2]  # Добавлен тест для проверки отрицательного индекса конца среза



