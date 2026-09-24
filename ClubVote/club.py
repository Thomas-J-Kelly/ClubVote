import math
import datetime



class Club:
    def __init__(self, members=None, voting_round=None):
        self.members = members if members is not None else []
        self.voting_round = voting_round if voting_round is not None else []

    def add_member(self, member):
        self.members.append(member)
    
    def add_voting_round(self, voting_round):
        self.voting_round.append(voting_round)

class Member:
    def __init__(self, name, ID=None):
        self.name = name
        self.ID = ID
    
class Candidate:
    def __init__(self, name, nominator=None):
        self.name = name
        self.nominator = nominator  
        
class Ballot:
    def __init__(self, member, ranked_choices=None):
        self.member = member
        if ranked_choices is None:
            ranked_choices = []
        if len(ranked_choices) != 3:
            raise ValueError("A ballot must have 3 ranked choices.")
        elif len(set(ranked_choices)) != len(ranked_choices):
            raise ValueError("A ballot cannot have duplicate ranked choices.")
        else:
            self.ranked_choices = ranked_choices

class VotingRound:
    def __init__(self, start_time, end_time, ballots=None, candidates=None, results=None, winner=None):
        self.start_time = start_time
        self.end_time = end_time
        self.ballots = ballots if ballots is not None else []
        self.candidates = candidates if candidates is not None else []
        self.results = results if results is not None else {}
        self.winner = winner
        
    def add_candidate(self, candidate):
        self.candidates.append(candidate)
        self.results[candidate] = 0

    def add_ballot(self, ballot):
        current_time = datetime.date.today()
        for b in ballot.ranked_choices:
            if b not in self.candidates:
                raise ValueError(f"Candidate {b.name} is not in the list of candidates for this voting round.")
        if ballot.member.ID not in [b.member.ID for b in self.ballots]:
            if self.start_time <= current_time <= self.end_time:
                self.ballots.append(ballot)
            else:
                raise ValueError("Voting is not currently open.")
        else:
            raise ValueError(f"Member {ballot.member.name} has already submitted a ballot for this voting round.")

    def get_winner(self):
        if not self.results:
            raise ValueError("No votes have been tallied yet.")
        max_votes = max(self.results.values())
        winners = [candidate for candidate, votes in self.results.items() if votes == max_votes]
        if len(winners) == 1:
            self.winner = winners[0]
            return self.winner
        elif len(winners) > 1:
            for candidate in winners:
                print(f"Tie: {candidate.name} with {max_votes} votes.")
            runoff_round = VotingRound(start_time=datetime.date.today(), end_time=datetime.date.today() + datetime.timedelta(days=7))
            for candidate in winners:
                runoff_round.add_candidate(candidate)
            return runoff_round

    def tally_votes(self):
        
        for candidate in self.results:
            self.results[candidate] = 0
        for ballot in self.ballots:
            for rank, candidate in enumerate(ballot.ranked_choices, start=1):
                self.results[candidate] += math.ceil(3 / rank)
        for candidate, votes in self.results.items():
            print(f"{candidate.name}: {votes} votes")

club = Club()
bob = Member("Bob", 1)
club.add_member(bob)
dark_knight = Candidate("Dark Knight", nominator=bob)
angry_men = Candidate("12 Angry Men", nominator=bob)
persona = Candidate("Persona", nominator=bob)
minions = Candidate("Minions", nominator=bob)
september_voting_round = VotingRound(start_time=datetime.date(2026, 9, 1), end_time=datetime.date(2026, 9, 30))


john = Member("John", 2)
club.add_member(john)
john_ballot_september = Ballot(john, ranked_choices=[persona, angry_men, dark_knight])
september_voting_round.add_candidate(dark_knight)
september_voting_round.add_candidate(angry_men)
september_voting_round.add_candidate(persona)
september_voting_round.add_candidate(minions)
september_voting_round.add_ballot(john_ballot_september)




joy = Member("Joy", 3)
club.add_member(joy)
joy_ballot_september = Ballot(joy, ranked_choices=[angry_men, persona, dark_knight])
september_voting_round.add_ballot(joy_ballot_september)
bob_ballot_september = Ballot(bob, ranked_choices=[dark_knight, angry_men, persona])
september_voting_round.add_ballot(bob_ballot_september)
club.add_voting_round(september_voting_round)


joy_ballot_august = Ballot(joy, ranked_choices=[angry_men, persona, dark_knight])
john_ballot_august = Ballot(john, ranked_choices=[persona, angry_men, dark_knight])
bob_ballot_august = Ballot(bob, ranked_choices=[dark_knight, minions, persona])




september_voting_round.tally_votes()
september_voting_round.get_winner()



