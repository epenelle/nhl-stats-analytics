# This script parses a csv file and prints the first 10 lines of the file to the console.
# Usage: python parse_csv.py <csv_file>
import csv
import os
import requests
from dotenv import load_dotenv

class SkaterSeasonStats:
    def __init__(self, all, fiveOnfive, fiveOnFour, fourOnfive, other):
        self.all = all
        self.five_on_five = fiveOnfive
        self.five_on_four = fiveOnFour
        self.four_on_five = fourOnfive
        self.other = other

        self.playerId = self.all.playerId
        self.season = self.all.season
        self.name = self.all.name
        self.team = self.all.team
        self.position = self.all.position

        self.games_played = self.all.games_played
        self.icetime = self.all.icetime
        self.shifts = self.all.shifts
        self.gameScore = self.all.gameScore
        self.onIce_corsiPercentage = self.all.onIce_corsiPercentage
        self.I_F_primaryAssists = self.all.I_F_primaryAssists
        self.I_F_secondaryAssists = self.all.I_F_secondaryAssists
        self.I_F_shotsOnGoal = self.all.I_F_shotsOnGoal
        self.I_F_missedShots = self.all.I_F_missedShots
        self.I_F_shotAttempts = self.all.I_F_shotAttempts
        self.I_F_goals = self.all.I_F_goals
        self.I_F_rebounds = self.all.I_F_rebounds
        self.I_F_reboundGoals = self.all.I_F_reboundGoals
        self.I_F_hits = self.all.I_F_hits
        self.I_F_takeaways = self.all.I_F_takeaways
        self.I_F_giveaways = self.all.I_F_giveaways
        self.I_F_lowDangerShots = self.all.I_F_lowDangerShots
        self.I_F_mediumDangerShots = self.all.I_F_mediumDangerShots
        self.I_F_highDangerShots = self.all.I_F_highDangerShots
        self.I_F_lowDangerGoals = self.all.I_F_lowDangerGoals
        self.I_F_mediumDangerGoals = self.all.I_F_mediumDangerGoals
        self.I_F_highDangerGoals = self.all.I_F_highDangerGoals
        self.shotsBlockedByPlayer = self.all.shotsBlockedByPlayer
        self.FiveOnFourPts = (self.five_on_four.I_F_goals + self.five_on_four.I_F_primaryAssists + self.five_on_four.I_F_secondaryAssists)
        self.FiveOnFourIcetime = self.five_on_four.icetime
        self.FourOnFivePts = (self.four_on_five.I_F_goals + self.four_on_five.I_F_primaryAssists + self.four_on_five.I_F_secondaryAssists)
        self.FourOnFiveIcetime = self.four_on_five.icetime

        self.YF_Goal = float(os.environ['YF_GOALS_PTS']) * self.I_F_goals
        self.YF_Assist = float(os.environ['YF_ASSISTS_PTS']) * (self.I_F_primaryAssists + self.I_F_secondaryAssists)
        self.YF_Shot = round(float(os.environ['YF_SHOT_PTS']) * self.I_F_shotsOnGoal)
        self.YF_Hit = round(float(os.environ['YF_HIT_PTS']) * self.I_F_hits)
        self.YF_Block = round(float(os.environ['YF_BLOCK_PTS']) * self.shotsBlockedByPlayer)
        self.YF_FiveOnFour = round(float(os.environ['YF_FIVEONFOUR_PTS']) * (self.five_on_four.I_F_goals + self.five_on_four.I_F_primaryAssists + self.five_on_four.I_F_secondaryAssists))
        self.YF_FourOnFive = round(float(os.environ['YF_FOURONFIVE_PTS']) * (self.four_on_five.I_F_goals + self.four_on_five.I_F_primaryAssists + self.four_on_five.I_F_secondaryAssists))
        self.YF_Pts = self.YF_Goal + self.YF_Assist + self.YF_Shot + self.YF_Hit + self.YF_Block + self.YF_FiveOnFour + self.YF_FourOnFive
        self.YF_PtsPer60 = self.YF_Pts * 60 / (self.icetime/60) #ice time = seconds, convert to minutes

class SkaterSeasonStatsPrediction:
    playerId = None
    season = 2023
    name = None
    team = None
    position = None
    games_played = None
    icetime = None
    shifts = None
    gameScore = None
    onIce_corsiPercentage = None
    I_F_primaryAssists = None
    I_F_secondaryAssists = None
    I_F_shotsOnGoal = None
    I_F_missedShots = None
    I_F_shotAttempts = None
    I_F_goals = None
    I_F_rebounds = None
    I_F_reboundGoals = None
    I_F_hits = None
    I_F_takeaways = None
    I_F_giveaways = None
    I_F_lowDangerShots = None
    I_F_mediumDangerShots = None
    I_F_highDangerShots = None
    I_F_lowDangerGoals = None
    I_F_mediumDangerGoals = None
    I_F_highDangerGoals = None
    shotsBlockedByPlayer = None
    FiveOnFourPts = None
    FiveOnFourIcetime = None
    FourOnFivePts = None
    FourOnFiveIcetime = None
    YF_Goal = None
    YF_Assist = None
    YF_Shot = None
    YF_Hit = None
    YF_Block = None
    YF_FiveOnFour = None
    YF_FourOnFive = None
    YF_Pts = None
    YF_PtsPer60 = None
        
    def __init__(self, skaterSeasonStats: SkaterSeasonStats=None):
        self.playerId = skaterSeasonStats.playerId
        self.name = skaterSeasonStats.name
        self.team = skaterSeasonStats.team
        self.position = skaterSeasonStats.position


# class SkaterSituationSeasonStats:
class SkaterSituationSeasonStats:
    def __init__(self,
                playerId,
                season,
                name,
                team,
                position,
                situation,
                games_played,
                icetime,
                shifts,
                gameScore,
                onIce_corsiPercentage,
                I_F_primaryAssists,
                I_F_secondaryAssists,
                I_F_shotsOnGoal,
                I_F_missedShots,
                I_F_shotAttempts,
                I_F_goals,
                I_F_rebounds,
                I_F_reboundGoals,
                I_F_hits,
                I_F_takeaways,
                I_F_giveaways,
                I_F_lowDangerShots,
                I_F_mediumDangerShots,
                I_F_highDangerShots,
                I_F_lowDangerGoals,
                I_F_mediumDangerGoals,
                I_F_highDangerGoals,
                shotsBlockedByPlayer):
        self.playerId = playerId
        self.season = season
        self.name = name
        self.team = team
        self.position = position
        self.situation = situation
        self.games_played = float(games_played)
        self.icetime = float(icetime)
        self.shifts = float(shifts)
        self.gameScore = float(gameScore)
        self.onIce_corsiPercentage = float(onIce_corsiPercentage)
        self.I_F_primaryAssists = float(I_F_primaryAssists)
        self.I_F_secondaryAssists = float(I_F_secondaryAssists)
        self.I_F_shotsOnGoal = float(I_F_shotsOnGoal)
        self.I_F_missedShots = float(I_F_missedShots)
        self.I_F_shotAttempts = float(I_F_shotAttempts)
        self.I_F_goals = float(I_F_goals)
        self.I_F_rebounds = float(I_F_rebounds)
        self.I_F_reboundGoals = float(I_F_reboundGoals)
        self.I_F_hits = float(I_F_hits)
        self.I_F_takeaways = float(I_F_takeaways)
        self.I_F_giveaways = float(I_F_giveaways)
        self.I_F_lowDangerShots = float(I_F_lowDangerShots)
        self.I_F_mediumDangerShots = float(I_F_mediumDangerShots)
        self.I_F_highDangerShots = float(I_F_highDangerShots)
        self.I_F_lowDangerGoals = float(I_F_lowDangerGoals)
        self.I_F_mediumDangerGoals = float(I_F_mediumDangerGoals)
        self.I_F_highDangerGoals = float(I_F_highDangerGoals)
        self.shotsBlockedByPlayer = float(shotsBlockedByPlayer)

def GetAllPlayerSituationStats(allSkaterStats, season):
    # make a get request to the specified URL
    url = f"https://moneypuck.com/moneypuck/playerData/seasonSummary/{season}/regular/skaters.csv"
    result = requests.get(url)
    if result.status_code == 200:
        # write the contents of the response (the data) to a file
        csv_reader = csv.DictReader(result.iter_lines(decode_unicode=True))
        for row in csv_reader:
            skaterSeasonStats = SkaterSituationSeasonStats(
                row["playerId"],
                row["season"],
                row["name"],
                row["team"],
                row["position"],
                row["situation"],
                row["games_played"],
                row["icetime"],
                row["shifts"],
                row["gameScore"],
                row["onIce_corsiPercentage"],
                row["I_F_primaryAssists"],
                row["I_F_secondaryAssists"],
                row["I_F_shotsOnGoal"],
                row["I_F_missedShots"],
                row["I_F_shotAttempts"],
                row["I_F_goals"],
                row["I_F_rebounds"],
                row["I_F_reboundGoals"],
                row["I_F_hits"],
                row["I_F_takeaways"],
                row["I_F_giveaways"],
                row["I_F_lowDangerShots"],
                row["I_F_mediumDangerShots"],
                row["I_F_highDangerShots"],
                row["I_F_lowDangerGoals"],
                row["I_F_mediumDangerGoals"],
                row["I_F_highDangerGoals"],
                row["shotsBlockedByPlayer"]
            )
            # Check if player exists in dictionary
            if (allSkaterStats.get(skaterSeasonStats.playerId) == None):
                allSkaterStats[skaterSeasonStats.playerId] = {}

            # Check if season exists in dictionary
            if (allSkaterStats[skaterSeasonStats.playerId].get(season) == None):
                allSkaterStats[skaterSeasonStats.playerId][season] = {}

            allSkaterStats[skaterSeasonStats.playerId][season][skaterSeasonStats.situation] = skaterSeasonStats

    else:
        print(f"Error: could not retrieve data from URL {url}.")
        print(f"Status code: {result.status_code}")

    return 



def SituationStatsToSeasonStats(allSkaterStats, allSkaterSeasonStats, season):
    for playerId in allSkaterStats:
        if (allSkaterStats[playerId].get(season) == None):
            # print(f"Player {playerId} does not have stats for season {season}")
            continue
        skaterSituationsStats = allSkaterStats[playerId][season]
        skaterSeasonStats = SkaterSeasonStats(all=skaterSituationsStats["all"],
                                                fiveOnfive=skaterSituationsStats["5on5"],
                                                fiveOnFour=skaterSituationsStats["5on4"],
                                                fourOnfive=skaterSituationsStats["4on5"],
                                                other=skaterSituationsStats["other"])
        
        # Check if player exists in dictionary
        if (allSkaterSeasonStats.get(playerId) == None):
            allSkaterSeasonStats[playerId] = {}

        # Check if season exists in dictionary
        if (allSkaterSeasonStats[playerId].get(season) == None):
            allSkaterSeasonStats[playerId][season] = {}

        allSkaterSeasonStats[playerId][season] = skaterSeasonStats
    return

def WriteStatsToCsvFile(allSkaterSeasonStats, season):
    WriteToSingleSeasonStats(allSkaterSeasonStats, season)
    WriteToAllSeasonsStats(allSkaterSeasonStats)

def WriteToSingleSeasonStats(allSkaterSeasonStats, season):
    singleSeasonStatsFilePath = f"output/skaters_{season}.csv"
    if(os.path.exists(singleSeasonStatsFilePath)):
        return
    with open(singleSeasonStatsFilePath, 'w', newline='') as csv_file:
        fieldnames = ["playerId",
                        "name",
                        "season",
                        "team",
                        "position",
                        "games_played",
                        "icetime",
                        "shifts",
                        "gameScore",
                        "YF_Pts",
                        "YF_PtsPer60",
                        "YF_Goal",
                        "YF_Assist",
                        "YF_Shot",
                        "YF_Hit",
                        "YF_Block",
                        "YF_FiveOnFour",
                        "YF_FourOnFive",
                        "onIce_corsiPercentage",
                        "I_F_primaryAssists",
                        "I_F_secondaryAssists",
                        "I_F_shotsOnGoal",
                        "I_F_missedShots",
                        "I_F_shotAttempts",
                        "I_F_goals",
                        "I_F_rebounds",
                        "I_F_reboundGoals",
                        "I_F_hits",
                        "I_F_takeaways",
                        "I_F_giveaways",
                        "I_F_lowDangerShots",
                        "I_F_mediumDangerShots",
                        "I_F_highDangerShots",
                        "I_F_lowDangerGoals",
                        "I_F_mediumDangerGoals",
                        "I_F_highDangerGoals",
                        "shotsBlockedByPlayer",
                        "FiveOnFourPts",
                        "FourOnFivePts",
                        "FiveOnFourIcetime",
                        "FourOnFiveIcetime",
                        "YF_PtsPer60"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for playerId in allSkaterSeasonStats:
            if (allSkaterSeasonStats[playerId].get(season) == None):
                # print(f"Player {playerId} does not have stats for season {season}")
                continue
            skaterSeasonStats = allSkaterSeasonStats[playerId][season]
            writer.writerow({
                "playerId": skaterSeasonStats.playerId,
                "name": skaterSeasonStats.name,
                "season": skaterSeasonStats.season,
                "team": skaterSeasonStats.team,
                "position": skaterSeasonStats.position,
                "games_played": skaterSeasonStats.games_played,
                "icetime": skaterSeasonStats.icetime,
                "shifts": skaterSeasonStats.shifts,
                "gameScore": skaterSeasonStats.gameScore,
                "onIce_corsiPercentage": skaterSeasonStats.onIce_corsiPercentage,
                "I_F_primaryAssists": skaterSeasonStats.I_F_primaryAssists,
                "I_F_secondaryAssists": skaterSeasonStats.I_F_secondaryAssists,
                "I_F_shotsOnGoal": skaterSeasonStats.I_F_shotsOnGoal,
                "I_F_missedShots": skaterSeasonStats.I_F_missedShots,
                "I_F_shotAttempts": skaterSeasonStats.I_F_shotAttempts,
                "I_F_goals": skaterSeasonStats.I_F_goals,
                "I_F_rebounds": skaterSeasonStats.I_F_rebounds,
                "I_F_reboundGoals": skaterSeasonStats.I_F_reboundGoals,
                "I_F_hits": skaterSeasonStats.I_F_hits,
                "I_F_takeaways": skaterSeasonStats.I_F_takeaways,
                "I_F_giveaways": skaterSeasonStats.I_F_giveaways,
                "I_F_lowDangerShots": skaterSeasonStats.I_F_lowDangerShots,
                "I_F_mediumDangerShots": skaterSeasonStats.I_F_mediumDangerShots,
                "I_F_highDangerShots": skaterSeasonStats.I_F_highDangerShots,
                "I_F_lowDangerGoals": skaterSeasonStats.I_F_lowDangerGoals,
                "I_F_mediumDangerGoals": skaterSeasonStats.I_F_mediumDangerGoals,
                "I_F_highDangerGoals": skaterSeasonStats.I_F_highDangerGoals,
                "shotsBlockedByPlayer": skaterSeasonStats.shotsBlockedByPlayer,
                "FiveOnFourPts": skaterSeasonStats.FiveOnFourPts,
                "FourOnFivePts": skaterSeasonStats.FourOnFivePts,
                "YF_Goal": skaterSeasonStats.YF_Goal,
                "YF_Assist": skaterSeasonStats.YF_Assist,
                "YF_Shot": skaterSeasonStats.YF_Shot,
                "YF_Hit": skaterSeasonStats.YF_Hit,
                "YF_Block": skaterSeasonStats.YF_Block,
                "YF_FiveOnFour": skaterSeasonStats.YF_FiveOnFour,
                "YF_FourOnFive": skaterSeasonStats.YF_FourOnFive,
                "YF_Pts": skaterSeasonStats.YF_Pts,
                "FiveOnFourIcetime": skaterSeasonStats.FiveOnFourIcetime,
                "FourOnFiveIcetime": skaterSeasonStats.FourOnFiveIcetime,
                "YF_PtsPer60": skaterSeasonStats.YF_PtsPer60
            })

def WriteToAllSeasonsStats(allSkaterSeasonStats):
    # check if file exists
    allSeasonStatsFilePath = f"output/skaters_all.csv"
    
    with open(allSeasonStatsFilePath, 'a', newline='') as csv_file:
        fieldnames = ["playerId",
                        "name",
                        "season",
                        "team",
                        "position",
                        "games_played",
                        "icetime",
                        "shifts",
                        "gameScore",
                        "YF_Pts",
                        "YF_PtsPer60",
                        "YF_Goal",
                        "YF_Assist",
                        "YF_Shot",
                        "YF_Hit",
                        "YF_Block",
                        "YF_FiveOnFour",
                        "YF_FourOnFive",
                        "onIce_corsiPercentage",
                        "I_F_primaryAssists",
                        "I_F_secondaryAssists",
                        "I_F_shotsOnGoal",
                        "I_F_missedShots",
                        "I_F_shotAttempts",
                        "I_F_goals",
                        "I_F_rebounds",
                        "I_F_reboundGoals",
                        "I_F_hits",
                        "I_F_takeaways",
                        "I_F_giveaways",
                        "I_F_lowDangerShots",
                        "I_F_mediumDangerShots",
                        "I_F_highDangerShots",
                        "I_F_lowDangerGoals",
                        "I_F_mediumDangerGoals",
                        "I_F_highDangerGoals",
                        "shotsBlockedByPlayer",
                        "FiveOnFourPts",
                        "FourOnFivePts",
                        "FiveOnFourIcetime",
                        "FourOnFiveIcetime"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for playerId in allSkaterSeasonStats:
            for season in allSkaterSeasonStats[playerId]:
                skaterSeasonStats = allSkaterSeasonStats[playerId][season]

                writer.writerow({
                    "playerId": skaterSeasonStats.playerId,
                    "name": skaterSeasonStats.name,
                    "season": skaterSeasonStats.season,
                    "team": skaterSeasonStats.team,
                    "position": skaterSeasonStats.position,
                    "games_played": skaterSeasonStats.games_played,
                    "icetime": skaterSeasonStats.icetime,
                    "shifts": skaterSeasonStats.shifts,
                    "gameScore": skaterSeasonStats.gameScore,
                    "onIce_corsiPercentage": skaterSeasonStats.onIce_corsiPercentage,
                    "I_F_primaryAssists": skaterSeasonStats.I_F_primaryAssists,
                    "I_F_secondaryAssists": skaterSeasonStats.I_F_secondaryAssists,
                    "I_F_shotsOnGoal": skaterSeasonStats.I_F_shotsOnGoal,
                    "I_F_missedShots": skaterSeasonStats.I_F_missedShots,
                    "I_F_shotAttempts": skaterSeasonStats.I_F_shotAttempts,
                    "I_F_goals": skaterSeasonStats.I_F_goals,
                    "I_F_rebounds": skaterSeasonStats.I_F_rebounds,
                    "I_F_reboundGoals": skaterSeasonStats.I_F_reboundGoals,
                    "I_F_hits": skaterSeasonStats.I_F_hits,
                    "I_F_takeaways": skaterSeasonStats.I_F_takeaways,
                    "I_F_giveaways": skaterSeasonStats.I_F_giveaways,
                    "I_F_lowDangerShots": skaterSeasonStats.I_F_lowDangerShots,
                    "I_F_mediumDangerShots": skaterSeasonStats.I_F_mediumDangerShots,
                    "I_F_highDangerShots": skaterSeasonStats.I_F_highDangerShots,
                    "I_F_lowDangerGoals": skaterSeasonStats.I_F_lowDangerGoals,
                    "I_F_mediumDangerGoals": skaterSeasonStats.I_F_mediumDangerGoals,
                    "I_F_highDangerGoals": skaterSeasonStats.I_F_highDangerGoals,
                    "shotsBlockedByPlayer": skaterSeasonStats.shotsBlockedByPlayer,
                    "FiveOnFourPts": skaterSeasonStats.FiveOnFourPts,
                    "FourOnFivePts": skaterSeasonStats.FourOnFivePts,
                    "YF_Goal": skaterSeasonStats.YF_Goal,
                    "YF_Assist": skaterSeasonStats.YF_Assist,
                    "YF_Shot": skaterSeasonStats.YF_Shot,
                    "YF_Hit": skaterSeasonStats.YF_Hit,
                    "YF_Block": skaterSeasonStats.YF_Block,
                    "YF_FiveOnFour": skaterSeasonStats.YF_FiveOnFour,
                    "YF_FourOnFive": skaterSeasonStats.YF_FourOnFive,
                    "YF_Pts": skaterSeasonStats.YF_Pts,
                    "FiveOnFourIcetime": skaterSeasonStats.FiveOnFourIcetime,
                    "FourOnFiveIcetime": skaterSeasonStats.FourOnFiveIcetime,
                    "YF_PtsPer60": skaterSeasonStats.YF_PtsPer60
                })

def WriteDataToCsvFiles(seasonList, allSkaterSeasonStats):
    allSeasonStatsFilePath = f"output/skaters_all.csv"
    writeToAllSeason = not os.path.exists(allSeasonStatsFilePath)
    for season in seasonList:
        WriteToSingleSeasonStats(allSkaterSeasonStats, season)

    if(writeToAllSeason):
        WriteToAllSeasonsStats(allSkaterSeasonStats)

def Predict(allSkaterSeasonStats):
    for playerId in allSkaterSeasonStats:
        skaterAllSeasonsStats = allSkaterSeasonStats[playerId]
        skater2023SeasonStats = PredictBasedOnWeights(skaterAllSeasonsStats)
        if skater2023SeasonStats is not None:
            skaterAllSeasonsStats["2023"] = skater2023SeasonStats
            

        

def PredictBasedOnWeights(skaterAllSeasonsStats):
    weightsDict = GetWeightsSeasonDict(skaterAllSeasonsStats)
    skater2023SeasonStats = None
    if skaterAllSeasonsStats.get("2022") is not None:
        skater2023SeasonStats = SkaterSeasonStatsPrediction(skaterAllSeasonsStats["2022"])
    elif skaterAllSeasonsStats.get("2021") is not None:
        skater2023SeasonStats = SkaterSeasonStatsPrediction(skaterAllSeasonsStats["2021"])
    elif skaterAllSeasonsStats.get("2020") is not None:
        skater2023SeasonStats = SkaterSeasonStatsPrediction(skaterAllSeasonsStats["2020"])
    else:
        return None
    statKeys = ["games_played", 
                "icetime",
                "shifts",
                "gameScore",
                "onIce_corsiPercentage",
                "I_F_primaryAssists",
                "I_F_secondaryAssists",
                "I_F_shotsOnGoal",
                "I_F_missedShots",
                "I_F_shotAttempts",
                "I_F_goals",
                "I_F_rebounds",
                "I_F_reboundGoals",
                "I_F_hits",
                "I_F_takeaways",
                "I_F_giveaways",
                "I_F_lowDangerShots",
                "I_F_mediumDangerShots",
                "I_F_highDangerShots",
                "I_F_lowDangerGoals",
                "I_F_mediumDangerGoals",
                "I_F_highDangerGoals",
                "shotsBlockedByPlayer",
                "FiveOnFourPts",
                "FiveOnFourIcetime",
                "FourOnFivePts",
                "FourOnFiveIcetime",
                "YF_Goal",
                "YF_Assist",
                "YF_Shot",
                "YF_Hit",
                "YF_Block",
                "YF_FiveOnFour",
                "YF_FourOnFive",
                "YF_Pts",
                "YF_PtsPer60"]

    for statKey in statKeys:
        prediction = PredictStatBasedOnWeights(skaterAllSeasonsStats, statKey, weightsDict)
        setattr(skater2023SeasonStats, statKey, prediction)
    
    return skater2023SeasonStats
    

def PredictStatBasedOnWeights(skaterAllSeasonsStats, statKey, weightsDict):
    prediction = 0
    for weightKvp in weightsDict:
        season = weightKvp["season"]
        weight = weightKvp["weight"]
        prediction += getattr(skaterAllSeasonsStats[season], statKey) * weight
    return prediction


def GetWeightsSeasonDict(skaterAllSeasonStats):
    # HasPlayed returns true if the player have played at least 20 games during the season
    def HasPlayed(skaterAllSeasonStats, season):
        return skaterAllSeasonStats.get(season) is not None and int(skaterAllSeasonStats[season].games_played) >= 20

    weightsPerSeason = []
    # Edge cases
    # Missed last 2 seasons
    if(not HasPlayed(skaterAllSeasonStats, "2021") and not HasPlayed(skaterAllSeasonStats, "2022")):
        return weightsPerSeason
    
    # Missed last season (may be retired)
    if (not HasPlayed(skaterAllSeasonStats, "2022")):
        weightsPerSeason.append({"season":"2021", "weight":1})

    # Rookie
    elif(not HasPlayed(skaterAllSeasonStats, "2021") ):
        weightsPerSeason.append({"season":"2022", "weight":1.2})

    else:
        if(not HasPlayed(skaterAllSeasonStats, "2020")):
            weightsPerSeason.append({"season":"2021", "weight":0.3})
            weightsPerSeason.append({"season":"2022", "weight":0.7})
        else:
            weightsPerSeason.append({"season":"2020", "weight":0.10})
            weightsPerSeason.append({"season":"2021", "weight":0.25})
            weightsPerSeason.append({"season":"2022", "weight":0.65})
    return weightsPerSeason
        



def main():
    load_dotenv()

    # read all lines from config.txt into a list
    with open("config.txt", 'r') as seasons:
        seasonList = seasons.read().splitlines()

    allSkaterStats = {}
    allSkaterSeasonStats = {}
    for season in seasonList:
        GetAllPlayerSituationStats(allSkaterStats, season)
        SituationStatsToSeasonStats(allSkaterStats, allSkaterSeasonStats, season)
        
    Predict(allSkaterSeasonStats)

    WriteDataToCsvFiles(seasonList, allSkaterSeasonStats)

if __name__ == "__main__":
    main()