import pytest


class TestDemo:
    def test_1(self):
        assert 1 == 1

    def test_2(self):
        assert 1 == 21

    def test_3(self):
        print('test_3')
        assert 1 == 21

    def test_4(self):
        print('test_4')
        print('hello')
        assert 1 == 21


if __name__ == '__main__':
    pytest.main(['-sq', 'test.py'])
