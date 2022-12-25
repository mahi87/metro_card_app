import os

os.environ["DATABASE_URL"] = "sqlite://"

import unittest
from app import app, db
from app.models import MetroCard


class TestCreateMetroCardApi(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_should_create_metro_card_with_valid_values(self):
        with app.test_client() as client:
            response = client.post(
                "/v1/metro_card", json={"name": "mahima", "pin": "1234"}
            )
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json, {"id": 1})

    def test_should_return_error_when_pin_is_absent(self):
        with app.test_client() as client:
            response = client.post("/v1/metro_card", json={"name": "mahima"})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {"message": "missing name/pin args"})

    def test_should_return_error_when_name_is_absent(self):
        with app.test_client() as client:
            response = client.post("/v1/metro_card", json={"pin": "1234"})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {"message": "missing name/pin args"})


class GetMetroCard(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
        m1 = MetroCard(name="Mahima")
        m1.set_pin("1234")

        m2 = MetroCard(name="Mahi")
        m2.set_pin("1234")

        db.session.add(m1)
        db.session.add(m2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_should_return_all_metro_card(self):
        with app.test_client() as client:
            response = client.get("/v1/metro_card")

            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json,
                [
                    {"name": "Mahima", "id": 1, "balance": 0},
                    {"name": "Mahi", "id": 2, "balance": 0},
                ],
            )

    def test_should_return_metro_card_details_by_id(self):
        with app.test_client() as client:
            response = client.get("/v1/metro_card/1")

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {"name": "Mahima", "id": 1, "balance": 0})

    def test_should_return_404_when_id_does_not_exist(self):
        with app.test_client() as client:
            response = client.get("/v1/metro_card/3")

            self.assertEqual(response.status_code, 404)
