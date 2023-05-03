import unittest
from unittest.mock import MagicMock
from view import View


class TestView(unittest.TestCase):

    def setUp(self):
        self.controller_mock = MagicMock()
        self.view = View(self.controller_mock)

    def test_create_button(self):
        button = self.view.create_button("test_category", "50")
        self.assertEqual(button.cget("text"), "50$")
        self.assertEqual(button.cget("bg"), "purple")
        self.assertEqual(button.cget("fg"), "yellow")

    def test_check_answer(self):
        self.view.user_score = 0
        self.view.check_answer("Würzig", "Würzig", 100, self.view.user_score)
        self.assertEqual(self.view.user_score, 100)
        self.view.check_answer("False", "Würzig", 100, self.view.user_score)
        self.assertEqual(self.view.user_score, 100)


if __name__ == '__main__':
    unittest.main()