import unittest
import os
import database
from club import Member

TEST_DATABASE="test_club.db"

class TestDatabase(unittest.TestCase):
    def setUp(self):
        database.DATABASE_NAME = TEST_DATABASE
        database.create_tables()

    def tearDown(self):
        if os.path.exists(TEST_DATABASE):
            os.remove(TEST_DATABASE)
            
    def test_add_member(self):
        member = Member("Bob")
        database.add_member(member)
        self.assertEqual(member.ID, 1)

    def test_get_member(self):
        member = Member("Alice")
        database.add_member(member)
        retrieved_member = database.get_member(member.ID)
        self.assertEqual(retrieved_member.name, "Alice")