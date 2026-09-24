from club import Club, Member, Candidate, Ballot, VotingRound
import unittest
import datetime

class TestVotingRound(unittest.TestCase):
    def setUp(self):
        self.club = Club()
        self.bob = Member("Bob", 1)
        self.joy = Member("Joy", 2)
        self.gart = Member("Gart", 3)
        self.club.add_member(self.bob)
        self.club.add_member(self.joy)
        self.club.add_member(self.gart)
        self.dark_knight = Candidate("Dark Knight", self.bob)
        self.minions = Candidate("Minions", self.joy)
        self.persona = Candidate("Persona", self.joy)
        self.angry_men = Candidate("12 Angry Men", self.gart)
        self.septemberVotingRound = VotingRound(start_time = datetime.date.today(), end_time=datetime.date.today() + datetime.timedelta(days=7))
        self.septemberVotingRound.add_candidate(self.dark_knight)
        self.septemberVotingRound.add_candidate(self.angry_men)
        self.septemberVotingRound.add_candidate(self.persona)
        self.septemberVotingRound.add_candidate(self.minions)

    def test_valid_ballot(self):
        ballot = Ballot(
            self.bob,
            [self.dark_knight, self.angry_men, self.persona]
        )
        self.septemberVotingRound.add_ballot(ballot)
        self.assertIn(ballot, self.septemberVotingRound.ballots)

    def test_duplicate_ballot(self):
        ballot = Ballot(
            self.bob,
            [self.dark_knight, self.angry_men, self.persona]
        )
        ballot2 = Ballot(
            self.bob,
            [self.persona, self.dark_knight, self.angry_men]
        )
        self.septemberVotingRound.add_ballot(ballot)
        with self.assertRaises(ValueError):
            self.septemberVotingRound.add_ballot(ballot2)

    def test_invalid_candidate(self):
        bullet_train = Candidate("Bullet Train", self.gart)
        ballot = Ballot(
            self.gart,
            [bullet_train, self.dark_knight, self.persona]
        )
        with self.assertRaises(ValueError):
            self.septemberVotingRound.add_ballot(ballot)

    def test_wrong_number_of_choices(self):
        ballot=Ballot(
            self.joy,
            [self.persona]
        )
        with self.assertRaises(ValueError):
            self.septemberVotingRound.add_ballot(ballot)

    def test_closed_voting_round(self):
        self.closedVotingRound = VotingRound(start_time=datetime.date.today() - datetime.timedelta(days=2), end_time=datetime.date.today() - datetime.timedelta(days=1))
        ballot = Ballot(
            self.bob,
            [self.dark_knight, self.persona, self.minions]
        )
        with self.assertRaises(ValueError):
            self.closedVotingRound.add_ballot(ballot)

    def test_tally_votes(self):
        ballot = Ballot(
            self.bob,
            [self.dark_knight, self.persona, self.minions]
        )
        ballot2 = Ballot(
            self.joy,
            [self.persona, self.dark_knight, self.angry_men]
        )
        ballot3 = Ballot(
            self.gart,
            [self.dark_knight, self.angry_men, self.persona]
        )
        self.septemberVotingRound.add_ballot(ballot)
        self.septemberVotingRound.add_ballot(ballot2)
        self.septemberVotingRound.add_ballot(ballot3)
        self.septemberVotingRound.tally_votes()
        expected_results = {
            self.dark_knight: 8,
            self.angry_men: 3,
            self.persona: 6,
            self.minions: 1
        }

        self.assertEqual(
            self.septemberVotingRound.results,
            expected_results
        )

if __name__ == "__main__":
    unittest.main()


