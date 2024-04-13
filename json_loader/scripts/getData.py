import csv
import json
import os
import time
from defs import *

competitions.add(Competition("Premier League", 2, "England", "male", False, False))
competitions.add(Competition("La Liga", 11, "Spain", "male", False, False))

def readMatches():
    matchList = os.listdir('../matches')
    for file in matchList:
        with open(f'../matches/{file}', 'r', encoding='utf-8') as f:
            matchData = json.load(f)
            for match in matchData:
                stadium = None
                if match.get('stadium'):
                    stadium = match['stadium']['name']
                referee = None
                if match.get('referee'):
                    referee = match['referee']['name']
                homeManager = None
                if match['home_team'].get('managers'):
                    homeManager = match['home_team']['managers'][0]['name']
                awayManager = None
                if match['away_team'].get('managers'):
                    awayManager = match['away_team']['managers'][0]['name']

                countries.add(Country(
                    match['home_team']['country']['name'],
                    match['home_team']['country']['id']
                ))

                countries.add(Country(
                    match['away_team']['country']['name'],
                    match['away_team']['country']['id']
                ))

                if homeManager:
                    managers.add(Manager(
                        match['home_team']['managers'][0]['name'],
                        match['home_team']['managers'][0]['id'],
                        match['home_team']['managers'][0]['nickname'],
                        match['home_team']['managers'][0]['dob'],
                        match['home_team']['managers'][0]['country']['name']
                    ))
                    countries.add(Country(
                        match['home_team']['managers'][0]['country']['name'],
                        match['home_team']['managers'][0]['country']['id']
                    ))

                if awayManager:
                    managers.add(Manager(
                        match['away_team']['managers'][0]['name'],
                        match['away_team']['managers'][0]['id'],
                        match['away_team']['managers'][0]['nickname'],
                        match['away_team']['managers'][0]['dob'],
                        match['away_team']['managers'][0]['country']['name']
                    ))
                    countries.add(Country(
                        match['away_team']['managers'][0]['country']['name'],
                        match['away_team']['managers'][0]['country']['id']
                    ))

                teams.add(Team(
                    match['home_team']['home_team_name'],
                    match['home_team']['home_team_id'],
                    match['home_team']['home_team_gender'],
                    match['home_team']['home_team_group'],
                    match['home_team']['country']['name'],
                    homeManager
                ))
                teams.add(Team(
                    match['away_team']['away_team_name'],
                    match['away_team']['away_team_id'],
                    match['away_team']['away_team_gender'],
                    match['away_team']['away_team_group'],
                    match['away_team']['country']['name'],
                    awayManager
                ))

                if stadium:
                    stadiums.add(Stadium(
                        stadium,
                        match['stadium']['id'],
                        match['stadium']['country']['name']
                    ))
                    countries.add(Country(
                        match['stadium']['country']['name'],
                        match['stadium']['country']['id']
                    ))
                
                if referee:
                    referees.add(Referee(
                        referee,
                        match['referee']['id'],
                        match['referee']['country']['name']
                    ))
                    countries.add(Country(
                        match['referee']['country']['name'],
                        match['referee']['country']['id']
                    ))

                matches.add(Match(
                    match['match_id'],
                    match['season']['season_name'],
                    match['competition']['competition_name'],
                    match['match_date'],
                    match['kick_off'],
                    match['home_team']['home_team_name'],
                    match['away_team']['away_team_name'],
                    match['home_score'],
                    match['away_score'],
                    match['match_week'],
                    match['competition_stage']['name'],
                    stadium,
                    referee
                ))

def readLineups():
    for match in matches:
        with open(f"../lineups/{match.id}.json", encoding='utf-8') as file:
            lineupData = json.load(file)
            for lineup in lineupData:
                teamName = lineup['team_name']
                for player in lineup['lineup']:
                    players.add(Player(
                        player['player_name'],
                        player['player_id'],
                        player['jersey_number'],
                        teamName
                    ))
                    for card in player['cards']:
                        cards.add(Card(
                            player['player_name'],
                            match.id,
                            match.season,
                            match.competition,
                            card['time'],
                            card['card_type'],
                            card['reason'],
                            card['period']
                        ))
                    for position in player['positions']:
                        positions.add(Position(
                            match.id,
                            match.season,
                            match.competition,
                            player['player_name'],
                            position['position_id'],
                            position['position'],
                            position['from'],
                            position['to'],
                            position['from_period'],
                            position['to_period'],
                            position['start_reason'],
                            position['end_reason']
                        ))
                    lineups.add(Lineup(
                        match.id,
                        match.season,
                        match.competition,
                        teamName,
                        player['player_name'],
                    ))
                    countries.add(Country(
                        player['country']['name'],
                        player['country']['id']
                    ))

def readEvents():   
    for match in matches:
        with open(f"../events/{match.id}.json", encoding='utf-8') as file:
            eventData = json.load(file)
            for event in eventData:
                id = event.get('id')
                match_id = match.id
                season = match.season
                competition = match.competition
                indx = event.get('index')
                period = event.get('period')
                timestamp = event.get('timestamp')
                minute = event.get('minute')
                second = event.get('second')
                team = event.get('team', {}).get('name')
                player = event.get('player', {}).get('name')
                type_id = event['type']['id']
                type_name = event['type']['name']
                possession = event.get('possession')
                possession_team = event.get('possession_team', {}).get('name')
                pattern_id = event.get('play_pattern', {}).get('id')
                pattern_name = event.get('play_pattern', {}).get('name')
                loc_x = event.get('location', [None, None])[0]
                loc_y = event.get('location', [None, None])[1]
                duration = event.get('duration')
                counterattack = bool(event.get('counterpress'))
                
                # every event added here
                events.add(Event(
                    id,
                    match_id,
                    season,
                    competition,
                    indx,
                    period,
                    timestamp,
                    minute,
                    second,
                    team,
                    player,
                    type_id,
                    type_name,
                    possession,
                    possession_team,
                    pattern_id,
                    pattern_name,
                    loc_x,
                    loc_y,
                    duration,
                    counterattack
                ))

                # adding formations
                if event.get('tactics'):
                    formations.add(Formation(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        event['tactics'].get('formation')
                    ))

                # Adding Shot events
                if type_name == 'Shot':
                    endLoc = event['shot'].get('end_location', [None, None, None])
                    if endLoc[0] is not None:
                        if len(endLoc) == 2:
                            endLocX = endLoc[0]
                            endLocY = endLoc[1]
                            endLocZ = None
                        if len(endLoc) == 3:
                            endLocX = endLoc[0]
                            endLocY = endLoc[1]
                            endLocZ = endLoc[2]
                    shots.add(Shot(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        event['shot'].get('statsbomb_xg'),
                        endLocX,
                        endLocY,
                        endLocZ,
                        bool(event['shot'].get('follows_dribble')),
                        bool(event['shot'].get('first_time')),
                        bool(event['shot'].get('open_goal')),
                        bool(event['shot'].get('deflected')),
                        event['shot'].get('technique', {}).get('id'),
                        event['shot'].get('technique', {}).get('name'),
                        event['shot'].get('body_part', {}).get('id'),
                        event['shot'].get('body_part', {}).get('name'),
                        event['shot'].get('outcome', {}).get('id'),
                        event['shot'].get('outcome', {}).get('name'),
                    ))

                    #adding freeze frames
                    for frame in event['shot'].get('freeze_frame', []):
                        freeze_frames.add(FreezeFrame(
                            id,
                            match_id,
                            season,
                            competition,
                            frame['location'][0],
                            frame['location'][1],
                            frame['player']['name'],
                            bool(frame.get('teammate'))
                        ))

                #adding pass event
                if type_name == 'Pass':
                    passes.add(Pass(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        event['pass'].get('recipient', {}).get('name'),
                        event['pass'].get('length'),
                        event['pass'].get('angle'),
                        event['pass'].get('height_id'),
                        event['pass'].get('height_name'),
                        bool(event['pass'].get('aerial_won')),
                        event['pass'].get('end_location', [None, None])[0],
                        event['pass'].get('end_location', [None, None])[1],
                        event['pass'].get('assisted_shot_id'),
                        bool(event['pass'].get('deflected')),
                        bool(event['pass'].get('miscommunication')),
                        bool(event['pass'].get('cross')),
                        bool(event['pass'].get('cut_back')),
                        bool(event['pass'].get('switch')),
                        bool(event['pass'].get('shot_assist')),
                        bool(event['pass'].get('goal_assist')),
                        event['pass'].get('body_part', {}).get('id'),
                        event['pass'].get('body_part', {}).get('name'),
                        event['pass'].get('outcome', {}).get('id'),
                        event['pass'].get('outcome', {}).get('name'),
                        event['pass'].get('technique', {}).get('id'),
                        event['pass'].get('technique', {}).get('name')
                    ))

                #Adding bad behaviour events
                if type_name == 'Bad Behaviour':
                    bad_behaviours.add(BadBehaviour(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        event['bad_behaviour'].get('card', {}).get('id'),
                        event['bad_behaviour'].get('card', {}).get('name')
                    ))
                
                #Adding foul events
                if type_name == 'Foul Committed':
                    foul = event.get('foul_committed', {})
                    fouls.add(Foul(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        bool(foul.get('offensive')),
                        foul.get('foul_committed', {}).get('type', {}).get('id'),
                        foul.get('foul_committed', {}).get('type', {}).get('name'),
                        bool(foul.get('advantage')),
                        bool(foul.get('penalty')),
                        foul.get('card', {}).get('id'),
                        foul.get('card', {}).get('name')
                    ))

                #Adding foul won events
                if type_name == 'Foul Won':
                    foul = event.get('foul_won', {})
                    fouls_won.add(FoulWon(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        bool(foul.get('defensive')),
                        bool(foul.get('advantage')),
                        bool(foul.get('penalty')),
                    ))

                #adding dribble event
                if type_name == 'Dribble':
                    dribble = event['dribble']
                    dribbles.add(Dribble(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        bool(dribble.get('overrun')),
                        bool(dribble.get('nutmeg')),
                        dribble.get('outcome', {}).get('id'),
                        dribble.get('outcome', {}).get('name'),
                        bool(dribble.get('no_touch'))
                    ))

                #adding ball recovery event
                if type_name == 'Ball Recovery':
                    ball_recovery = event.get('ball_recovery', {})
                    ball_recoveries.add(BallRecovery(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        bool(ball_recovery.get('offensive')),
                        bool(ball_recovery.get('recovery_failure'))
                    ))

                #adding ball receipt event
                if type_name == 'Ball Receipt*':
                    ball_receipt = event.get('ball_receipt', {})
                    ball_receipts.add(BallReceipt(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        ball_receipt.get('outcome', {}).get('id'),
                        ball_receipt.get('outcome', {}).get('name')
                    ))

                #adding carry event
                if type_name == 'Carry':
                    carry = event['carry']
                    carries.add(Carry(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        carry.get('end_location', [None, None])[0],
                        carry.get('end_location', [None, None])[1]
                    ))

                #adding block event
                if type_name == 'Block':
                    block = event.get('block', {})
                    blocks.add(Block(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        bool(block.get('deflection')),
                        bool(block.get('offensive')),
                        bool(block.get('save_block'))
                    ))

                #adding duel event
                if type_name == 'Duel':
                    duel = event['duel']
                    duels.add(Duel(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        duel.get('outcome', {}).get('id'),
                        duel.get('outcome', {}).get('name')
                    ))

                #adding clearance event
                if type_name == 'Clearance':
                    clearance = event['clearance']
                    clearances.add(Clearance(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        bool(clearance.get('aerial_won')),
                        clearance.get('body_part', {}).get('id'),
                        clearance.get('body_part', {}).get('name')
                    ))

                #adding substitution event
                if type_name == 'Substitution':
                    substitution = event['substitution']
                    substitutions.add(Substitution(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        substitution.get('replacement', {}).get('name'),
                        substitution.get('outcome', {}).get('id'),
                        substitution.get('outcome', {}).get('name')
                    ))

                #adding interceptions
                if type_name == 'Interception':
                    interception = event['interception']
                    interceptions.add(Interception(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        interception.get('outcome', {}).get('id'),
                        interception.get('outcome', {}).get('name')
                    ))

                #adding goalkeeper event
                if type_name == 'Goal Keeper':
                    goalkeeper = event['goalkeeper']
                    goalkeepers.add(Goalkeeper(
                        id,
                        type_id,
                        type_name,
                        match_id,
                        season,
                        competition,
                        team,
                        player,
                        goalkeeper.get('position', {}).get('id'),
                        goalkeeper.get('position', {}).get('name'),
                        goalkeeper.get('technique', {}).get('id'),
                        goalkeeper.get('technique', {}).get('name'),
                        goalkeeper.get('body_part', {}).get('id'),
                        goalkeeper.get('body_part', {}).get('name'),
                        goalkeeper.get('outcome', {}).get('id'),
                        goalkeeper.get('outcome', {}).get('name')
                    ))
                
def writeDataToCSV():
    for key, value in allSets.items():
        with open(f'../collective_data/{key}.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            attrs = list(value)[0].__dict__.keys()
            writer.writerow(attrs)
            for item in value:
                writer.writerow(item.__dict__.values())


def populateData():
    readMatches()
    readLineups()
    readEvents()

def main():
    now = time.time()
    readMatches()
    readLineups()
    readEvents()
    writeDataToCSV()
    print(time.time() - now)

