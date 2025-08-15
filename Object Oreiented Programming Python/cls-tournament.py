# 10. Method Logic Challenge
# Create a Tournament class:
# Constructor takes team_names (list of strings).
# Method schedule_matches() returns all possible match combinations between teams without repetition.
# Method total_matches() returns the number of matches possible.
from itertools import combinations
class Tournament:
    def __init__(self , teams):
        self.teams = teams
    def schedule_matches(self):
        return list(combinations(teams, 2))
        

    def total_mataches(self):
        n = len(self.teams)
        total_matches = n*(n-1)//2
        return total_matches
    


teams = ["Pakistan" , "India" , "Australia" , "England" , "New Zealand" , "Afghanistan"]
tournament = Tournament(teams)
print(f"Total possible matches are : {tournament.total_mataches()}")
print(f"Matches between teams are :")

for match in tournament.schedule_matches():
    print(f"{match[0]} vs {match[1]}")
