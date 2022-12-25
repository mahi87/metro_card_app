import unittest
from unittest.mock import MagicMock
from app.models import MetroCard


class TestModels(unittest.TestCase):
    def test_should_hash_pin(self):
        m = MetroCard(name="Mahima")
        pin = "1234"
        m.set_pin(pin)
        self.assertTrue(m.check_pin(pin))
