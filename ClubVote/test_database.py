import unittest
import os
import database
from club import Member

TEST_DATABASE="test_club.db"

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.original_database =database.DATABASE_NAME
        database.DATABASE_NAME = TEST_DATABASE
        database.create_tables()

    def tearDown(self):
        if os.path.exists(TEST_DATABASE):
            os.remove(TEST_DATABASE)
        database.DATABASE_NAME = self.original_database
            
    def test_add_member(self):
        member = Member("Bob")
        database.add_member(member)
        self.assertEqual(member.ID, 1)

    def test_get_member(self):
        member = Member("Alice")
        database.add_member(member)
        retrieved_member = database.get_member(member.ID)
        self.assertEqual(retrieved_member.name, "Alice")
        self.assertEqual(retrieved_member.ID, member.ID)
        