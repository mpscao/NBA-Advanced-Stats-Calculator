
from typing import IO, List
# player profile that will consist of the player name and 10 raw stats
class Player:
    def __init__(self, name: str,
                 fgm: int,
                 fga: int,
                 threepm: int,
                 fta: int,
                 tov: int,
                 mp: int,
                 tmMp: int,
                 tmFga: int,
                 tmFta: int,
                 tmTov: int):
        # instantiate player name
        self.name = name
        # instantiate player's total number of field goals made
        self.fgm = fgm
        # instantiate player's total number of field goals attempted
        self.fga = fga
        # instantiate player's total number of three pointers made
        self.threepm = threepm
        # instantiate player's total number of free throws attempted
        self.fta = fta
        # instantiate player's total number of turnovers
        self.tov = tov
        # instantiate player's total number minutes played
        self.mp = mp
        # instantiate player's team's total number of minutes played
        self.tmMp = tmMp
        # instantiate player's team's total number of field goals attempted
        self.tmFga = tmFga
        # instantiate player's team's total number of free throws attempted
        self.tmFta = tmFta
        # instantiate player's team's total number of turnovers
        self.tmTov = tmTov

def open_file() -> IO:
    # ask for the file that contains the raw stats
    file_name = input("Enter a filename: ")
    # to ensure file in not changeable
    file_pointer = None
    while file_pointer is None:
        try:
            # try to open and read the file with given pointer is loaded in program
            file_pointer = open(file_name, "r")
        except IOError:
            # except if the file can't be opened, let user know there is an error and ask for filename again
            file_name = input("Error, please enter filename again: ")

    # return the pointer to the file
    return file_pointer


def create_players(nba_fp: IO) -> List[Player]:
    # create an empty list that will contain all the players
    players = []
    # read the first line to get number of players
    n = nba_fp.readline()
    n = int(n)
    # read the next line, which will be the first player
    line = nba_fp.readline()
    # get each stat for first player, which is separated by a space
    player_stats = line.split(' ')
    # for each player in the file
    for player in range(n):
        # get the player's name
        name = player_stats[0].strip()
        # get the player's total number of field goals made
        fgm = player_stats[1].strip()
        # get the player's total number of field goals attempted
        fga = player_stats[2].strip()
        # get the player's total number of three pointers made
        threepm = player_stats[3].strip()
        # get the player's total number of free throws attempted
        fta = player_stats[4].strip()
        # get the player's total number of turnovers
        tov = player_stats[5].strip()
        # get the player's total number of minutes played
        mp = player_stats[6].strip()
        # get the player's team's total number of minutes played
        tmMp = player_stats[7].strip()
        # get the player's team's total number of field goals attempted
        tmFga = player_stats[8].strip()
        # get the player's team's total number of free throws attempted
        tmFta = player_stats[9].strip()
        # get the player's team's total number of turnovers
        tmTov = player_stats[10].strip()
        # add each stat accordingly to the player's index in the list
        players.append(Player(name, fgm, fga, threepm, fta, tov, mp, tmMp, tmFga, tmFta, tmTov))
        # read the next player as long as there are still players
        line = nba_fp.readline()
        # get each stat for the next player, which is separated by a space
        player_stats = line.split(' ')

    return players
def effective_field_goal(player_list: List[Player]) -> List[List[str]]:
    # create an empty list effective field goal percentages
    efg = []
    for i in range(len(player_list)):
        # for each player, create a nested empty list
        efg.append([])
    # for each player, get stats to make the formula more clear and have less code
    for player in range(len(player_list)):
        # get the player's name from the list of players
        name = player_list[player].name
        # get the player's fgm from the list of players
        fgm = int(player_list[player].fgm)
        # get the player's 3pm from the list of players
        threepm = int(player_list[player].threepm)
        # get the player's fga from the list of players
        fga = int(player_list[player].fga)
        # calculate the player's effective field goal percentage according to the formula
        percentage = 100*((fgm + (0.5 * threepm))/fga)
        # round the percentage to 2 decimal places
        percentage = round(percentage, 2)
        # use extend to add the player's name and his effective field goal percentage to the newly created list
        efg[player].extend([name, percentage])
    # compare each player's efg to every other player
    for first in range(len(efg)):
        # go from original first player up without repeating comparisons
        for sec in range(len(efg)-first-1):
            # if a player's efg is less than another player's
            if efg[sec][1] < efg[sec + 1][1]:
                # temporarily take the player with a smaller efg's position
                temp = efg[sec]
                # make the player with a smaller efg's position the player with a larger efg's position
                efg[sec] = efg[sec+1]
                # swap the player with the larger efg's position the samller player's original position
                efg[sec + 1] = temp

    return efg
def usage(player_list: List[Player]) -> List[List[str]]:
    # create an empty list for usages
    usg = []
    for i in range(len(player_list)):
        # for each player, create a nested empty list
        usg.append([])
    # for each player, get stats to make the formula more clear and have less code
    for player in range(len(player_list)):
        # get the player's name from the list of players
        name = player_list[player].name
        # get the player's fga from the list of players
        fga = int(player_list[player].fga)
        # get the player's fta from the list of players
        fta = int(player_list[player].fta)
        # get the player's tov from the list of players
        tov = int(player_list[player].tov)
        # get the player's tmMp from the list of players
        tmMp = int(player_list[player].tmMp)
        # get the player's mp from the list of players
        mp = int(player_list[player].mp)
        # get the player's tmFga from the list of players
        tmFga = int(player_list[player].tmFga)
        # get the player's tmFta from the list of players
        tmFta = int(player_list[player].tmFta)
        # get the player's tmTov from the list of players
        tmTov = int(player_list[player].tmTov)
        # calulate the player's usage rate according to the formula
        usage_rate = 100*(((fga+(0.44*fta)+tov)*(tmMp/5)) / (mp*(tmFga+(0.44*tmFta)+tmTov)))
        # round the usage rate to 2 decimal places
        usage_rate = round(usage_rate, 2)
        # use extend to add the player's name and his effective field goal percentage to the newly created list
        usg[player].extend([name, usage_rate])

    # compare each player's usg to every other player
    for first in range(len(usg)):
        # go from original first player up without repeating comparisons
        for sec in range(len(usg) - first - 1):
            # if a player's usg is less than another player's
            if usg[sec][1] < usg[sec + 1][1]:
                # temporarily take the player with a smaller usg's position
                temp = usg[sec]
                # make the player with a smaller usg's position the player with a larger efg's position
                usg[sec] = usg[sec + 1]
                # swap the player with the larger usg's position the smaller player's original position
                usg[sec + 1] = temp

    return usg

def main():
    print("Welcome to NBA stat ranker\n" )
    # open the file
    nba_fp = open_file()
    # create the list of players given the file pointer
    players_list = create_players(nba_fp)
    # to get the list of player's effective field goal percentages
    efgp = effective_field_goal(players_list)
    # to get the list of player's usage rates
    usgr = usage(players_list)
    # get the user's choice of if they want to rank usage, effective field goal, or both
    choice = input("If you would like to rank effective field goal percentage, enter efg. If you would like to rank\n"
    "usage, enter usg. If you would like to rank both, enter both: ")
    while choice != "efg" and choice != "usg" and choice != "both":
        # if the user does not enter one of the options given, let the user know
        print("Unknown input\n")
        # ask them for another choice
        choice = input("If you would like to rank effective field goal percentage, enter efg. If you would like to rank\n"
            "usage, enter usg. If you would like to rank both, enter both: ")

    if choice == "efg":
        print("\n")
        # if the user wants to rank effective field goal percentage, show the rankingg according to the
        # ordered list efg
        for player in range(len(efgp)):
            print(str(player + 1) + ". " + efgp[player][0] + " " + str(efgp[player][1]) + '\n')

    elif choice == "usg":
        print("\n")
        # if the user wants to rank effective field goal percentage, show the ranking of players according to the
        # ordered list usg
        for player in range(len(usgr)):
            print(str(player + 1) + ". " + usgr[player][0] + " " + str(usgr[player][1]) + '\n')

    elif choice == "both":
        print("\n")
        # if the user wants to rank both, rank the players according effective feld goal percentage first
        print("Effective Field Goal Percentage ranked: ")
        # show the ranking of players according to the ordered list efg
        for player in range(len(efgp)):
            print(str(player + 1) + ". " + efgp[player][0] + " " + str(efgp[player][1]) + '\n')
        # then rank players according to usage
        print("Usage ranked: ")
        # show the ranking of players according to the ordered list usg
        for player in range(len(usgr)):
            print(str(player + 1) + ". " + usgr[player][0] + " " + str(usgr[player][1]) + '\n')

if __name__ == "__main__":
    main()
