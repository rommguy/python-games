from src.language_features import generate_closure_updater, increment_num
import pytest


def test_check_closure():
    change_closure = generate_closure_updater()
    change_closure(2)
    change_closure(3)
    change_closure(4)
    print("*********************************************************************************************")
    print(change_closure(5))


@pytest.fixture
def simple_fixture():
    return 5


class TestClassFixtures:
    context_var = 10

    @pytest.fixture(autouse=True)
    def class_init_fixture(self):
        self.context_var = 10

    def test_bla(self, simple_fixture):
        assert simple_fixture == 5

    def test_increment_num(self, simple_fixture):
        assert increment_num(self.context_var) == 11
