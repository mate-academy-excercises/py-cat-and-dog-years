import pytest
from app.main import get_human_age


class TestPetToHumanAge:

    @pytest.mark.parametrize("cat_age,dog_age, expected", [
        pytest.param(14, 14, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(23, 24, [1, 2]),
        pytest.param(27, 28, [2, 2]),
        pytest.param(28, 29, [3, 3]),
    ]
    )
    def test_should_calculate_age_correctly(self, cat_age: int,
                                            dog_age: int,
                                            expected: list[int]) -> None:
        assert get_human_age(cat_age, dog_age) == expected
