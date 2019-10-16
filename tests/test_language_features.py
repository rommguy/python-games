from src.language_features import generate_closure_updater, increment_num, count_cpu
import pytest
import psutil
from unittest.mock import patch


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


class TestMocks:
    @patch("psutil.cpu_count", return_value=200)
    def test_cpu_count(self, bla):
        assert count_cpu() == 200
        assert psutil.cpu_count.called is True

    def test_cpu_count_with_pytest_mock_spy(self, mocker):
        original_cpu_count = psutil.cpu_count()
        mocker.spy(psutil, "cpu_count")
        assert count_cpu() == original_cpu_count
        assert psutil.cpu_count.call_count == 1

    def test_cpu_count_with_pytest_mock(self, mocker):
        original_cpu_count = psutil.cpu_count()
        update_cpu_count = original_cpu_count * 2
        mocker.patch("psutil.cpu_count", return_value=update_cpu_count)
        assert count_cpu() == update_cpu_count
        assert psutil.cpu_count.call_count == 1
