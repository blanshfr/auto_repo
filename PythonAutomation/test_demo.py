import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
  def test_first_pytest(self):
    print("It's my first attempt")

  def test_second_pytest(self):
    print("It's my 2nd attempt")

  def test_third_pytest(self):
    print("It's my 3rd attempt")

