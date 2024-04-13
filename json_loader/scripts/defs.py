countries = set()
competitions = set()
managers = set()
teams = set()
stadiums = set()
referees = set()
matches = set()
players = set()
lineups = set()
cards = set()
positions = set()
events = set()
formations = set()
shots = set()
passes = set()
bad_behaviours = set()
fouls = set()
fouls_won = set()
dribbles = set()
ball_recoveries = set()
ball_receipts = set()
carries = set()
blocks = set()
duels = set()
clearances = set()
substitutions = set()
interceptions = set()
goalkeepers = set()
freeze_frames = set()

allSets = {
    "countries": countries,
    "competitions": competitions,
    "managers": managers,
    "teams": teams,
    "stadiums": stadiums,
    "referees": referees,
    "matches": matches,
    "formations": formations,
    "players": players,
    "lineups": lineups,
    "cards": cards,
    "positions": positions,
    "events": events,
    "shots": shots,
    "passes": passes,
    "bad_behaviours": bad_behaviours,
    "fouls": fouls,
    "fouls_won": fouls_won,
    "dribbles": dribbles,
    "ball_recoveries": ball_recoveries,
    "ball_receipts": ball_receipts,
    "carries": carries,
    "blocks": blocks,  
    "duels": duels,
    "clearances": clearances,
    "substitutions": substitutions,
    "interceptions": interceptions,
    "goalkeepers": goalkeepers,
    "freeze_frames": freeze_frames
}

class Country:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def toString(self):
        return f"""
        name: {self.name}
        id: {self.id}
        """
    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, value: object) -> bool:
        return self.name == value.name

class Competition:
    def __init__(self, name, id, country, gender, youth, international):
        self.name = name
        self.id = id
        self.country = country
        self.gender = gender
        self.youth = youth
        self.international = international
    def toString(self):
        return f"""
        name: {self.name}
        id: {self.id}
        country_name: {self.country}
        gender: {self.gender}
        youth: {self.youth}
        international: {self.international}
        """
    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, value: object) -> bool:
        return self.name == value.name

class Season:
    def __init__(self, name, id, competition):
        self.name = name
        self.id = id
        self.competition = competition
    def toString(self):
        return f"""
        name: {self.name}
        id: {self.id}
        competition: {self.competition}
        """
    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, value: object) -> bool:
        return self.name == value.name

class Manager:
    def __init__(self, name, id, nickname, dob, country):
        self.name = name
        self.id = id
        self.nickname = nickname
        self.dob = dob
        self.country = country
    def toString(self):
        return f"""
        name: {self.name}
        id: {self.id}
        nickname: {self.nickname}
        dob: {self.dob}
        country: {self.country}
        """
    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, value: object) -> bool:
        return self.name == value.name

class Team:
    def __init__(self, name, id, gender, grp, country, manager):
        self.name = name
        self.id = id
        self.gender = gender
        self.grp = grp
        self.country = country
        self.manager = manager
    def toString(self):
        return f"""
        name: {self.name}
        id: {self.id}
        gender: {self.gender}
        grp: {self.grp}
        country: {self.country}
        manager: {self.manager}
        """
    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, value: object) -> bool:
        return self.name == value.name

class Stadium:
    def __init__(self, name, id, country):
        self.name = name
        self.id = id
        self.country = country
    def toString(self):
        return f"""
        name: {self.name}
        id: {self.id}
        country_id: {self.country}
        """
    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, value: object) -> bool:
        return self.name == value.name

class Referee:
    def __init__(self, name, id, country):
        self.name = name
        self.id = id
        self.country = country
    def toString(self):
        return f"""
        name: {self.name}
        id: {self.id}
        country_id: {self.country}
        """
    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, value: object) -> bool:
        return self.name == value.name

class Match:
    def __init__(self, id, season, competition, date, kick_off, home_team, away_team, home_score, away_score, week, competition_stage, stadium, referee):
        self.id = id
        self.season = season
        self.competition = competition
        self.date = date
        self.kick_off = kick_off
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score
        self.week = week
        self.competition_stage = competition_stage
        self.stadium = stadium
        self.referee = referee
    def toString(self):
        return f"""
        id: {self.id}
        season: {self.season}
        competition: {self.competition}
        date: {self.date}
        kick_off: {self.kick_off}
        home_team: {self.home_team}
        away_team: {self.away_team}
        home_score: {self.home_score}
        away_score: {self.away_score}
        week: {self.week}
        competition_stage: {self.competition_stage}
        stadium: {self.stadium}
        referee: {self.referee}
        """

class Player:
    def __init__(self, name, id, jersey, team):
        self.name = name
        self.id = id
        self.jersey = jersey
        self.team = team
    def toString(self):
        return f"""
        name: {self.name}
        id: {self.id}
        jersey: {self.jersey}
        team: {self.team}
        """
    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, value: object) -> bool:
        return self.name == value.name

class Lineup:
    def __init__(self, match_id, season, competition, team, player):
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
    def toString(self):
        return f"""
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        """
    
class Card:
    def __init__(self, player, match_id, season, competition, time, card_type, reason, period):
        self.player = player
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.time = time
        self.card_type = card_type
        self.reason = reason
        self.period = period

class Position:
    def __init__(self, match_id, season, competition, player, position_id, position, from_time, to_time, from_period, to_period, start_reason, end_reason):
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.player = player
        self.position_id = position_id
        self.position = position
        self.from_time = from_time
        self.to_time = to_time
        self.from_period = from_period
        self.to_period = to_period
        self.start_reason = start_reason
        self.end_reason = end_reason

class Event:
    def __init__(self, id, match_id, season, competition, indx, period, timestamp, minute, second, team, player, type_id, type_name, possession, possession_team, pattern_id, pattern_name, loc_x, loc_y, duration, counterattack):
        self.id = id
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.indx = indx
        self.period = period
        self.timestamp = timestamp
        self.minute = minute
        self.second = second
        self.team = team
        self.player = player
        self.type_id = type_id
        self.type_name = type_name
        self.possession = possession
        self.possession_team = possession_team 
        self.pattern_id = pattern_id
        self.pattern_name = pattern_name
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.duration = duration
        self.counterattack = counterattack
    def toString(self):
        return f"""
        id: {self.id}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        possession: {self.possession}
        possession_team: {self.possession_team}
        idx: {self.idx}
        periods: {self.periods}
        timestamp: {self.timestamp}
        minute: {self.minute}
        second: {self.second}
        type_id: {self.type_id}
        type_name: {self.type_name}
        pattern_id: {self.pattern_id}
        pattern_name: {self.pattern_name}
        loc_x: {self.loc_x}
        loc_y: {self.loc_y}
        duration: {self.duration}
        counterattack: {self.counterattack}
        """

class Formation:
    def __init__(self, event_id, id, name, match_id, season, competition, team, formation):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.formation = formation
    def toString(self):
        return f"""
        match_id: {self.match_id}
        team: {self.team}
        formation: {self.formation}
        """
    
class Shot:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, statsbomb_xg, loc_x, loc_y, loc_z, follows_dribble, first_time, open_net, deflected, technique_id, technique_name, body_id, body_name, outcome_id, outcome_name):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.statsbomb_xg = statsbomb_xg
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.loc_z = loc_z
        self.follows_dribble = follows_dribble
        self.first_time = first_time
        self.open_net = open_net
        self.deflected = deflected
        self.technique_id = technique_id
        self.technique_name = technique_name
        self.body_id = body_id
        self.body_name = body_name
        self.outcome_id = outcome_id
        self.outcome_name = outcome_name
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        statsbomb_xg: {self.statsbomb_xg}
        loc_x: {self.loc_x}
        loc_y: {self.loc_y}
        loc_z: {self.loc_z}
        follows_dribble: {self.follows_dribble}
        first_time: {self.first_time}
        open_net: {self.open_net}
        deflected: {self.deflected}
        technique_id: {self.technique_id}
        technique_name: {self.technique_name}
        body_id: {self.body_id}
        body_name: {self.body_name}
        outcome_id: {self.outcome_id}
        outcome_name: {self.outcome_name}
        """

class Pass:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, recipient, length, angle, height_id, height_name, aerial_won, loc_x, loc_y, assisted_shot_id, deflected, miscomm, crossed, cut_back, switch, shot_assist, goal_assist, body_id, body_name, outcome_id, outcome_name, technique_id, technique_name):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.recipient = recipient
        self.length = length
        self.angle = angle
        self.height_id = height_id
        self.height_name = height_name
        self.aerial_won = aerial_won
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.assisted_shot_id = assisted_shot_id
        self.deflected = deflected
        self.miscomm = miscomm
        self.crossed = crossed
        self.cut_back = cut_back
        self.switch = switch
        self.shot_assist = shot_assist
        self.goal_assist = goal_assist
        self.body_id = body_id
        self.body_name = body_name
        self.outcome_id = outcome_id
        self.outcome_name = outcome_name
        self.technique_id = technique_id
        self.technique_name = technique_name
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        recipient: {self.recipient}
        length: {self.length}
        angle: {self.angle}
        height_id: {self.height_id}
        height_name: {self.height_name}
        aerial_won: {self.aerial_won}
        loc_x: {self.loc_x}
        loc_y: {self.loc_y}
        assisted_shot_id: {self.assisted_shot_id}
        deflected: {self.deflected}
        miscomm: {self.miscomm}
        crossed: {self.crossed}
        cut_back: {self.cut_back}
        switch: {self.switch}
        shot_assist: {self.shot_assist}
        goal_assist: {self.goal_assist}
        body_id: {self.body_id}
        body_name: {self.body_name}
        outcome_id: {self.outcome_id}
        outcome_name: {self.outcome_name}
        technique_id: {self.technique_id}
        technique_name: {self.technique_name}
        """

class BadBehaviour:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, card_id, card_name):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.card_id = card_id
        self.card_name = card_name
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        card_id: {self.card_id}
        card_name: {self.card_name}
        """

class Foul:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, offensive, foul_id, foul_name, advantage, penalty, card_id, card_name):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.offensive = offensive
        self.foul_id = foul_id
        self.foul_name = foul_name
        self.advantage = advantage
        self.penalty = penalty
        self.card_id = card_id
        self.card_name = card_name
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        offensive: {self.offensive}
        foul_id: {self.foul_id}
        foul_name: {self.foul_name}
        advantage: {self.advantage}
        penalty: {self.penalty}
        card_id: {self.card_id}
        card_name: {self.card_name}
        """

class FoulWon:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, defensive, advantage, penalty):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.defensive = defensive
        self.advantage = advantage
        self.penalty = penalty
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        defensive: {self.defensive}
        advantage: {self.advantage}
        penalty: {self.penalty}
        """

class Dribble:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, overrun, nutmeg, outcome_id, outcome_name, no_touch):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.overrun = overrun
        self.nutmeg = nutmeg
        self.outcome_id = outcome_id
        self.outcome_name = outcome_name
        self.no_touch = no_touch
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        overrun: {self.overrun}
        nutmeg: {self.nutmeg}
        outcome_id: {self.outcome_id}
        outcome_name: {self.outcome_name}
        no_touch: {self.no_touch}
        """
    
class BallRecovery:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, offensive, failure):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.offensive = offensive
        self.failure = failure
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        offensive: {self.offensive}
        failure: {self.failure}
        """

class BallReceipt:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, outcome_id, outcome_name):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.outcome_id = outcome_id
        self.outcome_name = outcome_name
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        outcome_id: {self.outcome_id}
        outcome_name: {self.outcome_name}
        """
    
class Carry:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, loc_x, loc_y):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.loc_x = loc_x
        self.loc_y = loc_y
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        loc_x: {self.loc_x}
        loc_y: {self.loc_y}
        """

class Block:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, deflection, offensive, save):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.deflection = deflection
        self.offensive = offensive
        self.save = save
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        deflection: {self.deflection}
        offensive: {self.offensive}
        save: {self.save}
        """

class Duel:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, outcome_id, outcome_name):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.outcome_id = outcome_id
        self.outcome_name = outcome_name
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        outcome_id: {self.outcome_id}
        outcome_name: {self.outcome_name}
        """

class Clearance:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, aerial_won, body_id, body_name):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.aerial_won = aerial_won
        self.body_id = body_id
        self.body_name = body_name
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        aerial_won: {self.aerial_won}
        body_id: {self.body_id}
        body_name: {self.body_name}
        """

class Substitution:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, subbed_name, outcome_id, outcome_name):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.subbed_name = subbed_name
        self.outcome_id = outcome_id
        self.outcome_name = outcome_name
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        subbed_id: {self.subbed_id}
        subbed_name: {self.subbed_name}
        outcome_id: {self.outcome_id}
        outcome_name: {self.outcome_name}
        """

class Interception:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, outcome_id, outcome_name):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.outcome_id = outcome_id
        self.outcome_name = outcome_name
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        outcome_id: {self.outcome_id}
        outcome_name: {self.outcome_name}
        """

class Goalkeeper:
    def __init__(self, event_id, id, name, match_id, season, competition, team, player, pos_id, pos_name, technique_id, technique_name, body_id, body_name, outcome_id, outcome_name):
        self.event_id = event_id
        self.id = id
        self.name = name
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.team = team
        self.player = player
        self.pos_id = pos_id
        self.pos_name = pos_name
        self.technique_id = technique_id
        self.technique_name = technique_name
        self.body_id = body_id
        self.body_name = body_name
        self.outcome_id = outcome_id
        self.outcome_name = outcome_name
    def toString(self):
        return f"""
        event_id: {self.event_id}
        id: {self.id}
        name: {self.name}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        team: {self.team}
        player: {self.player}
        pos_id: {self.pos_id}
        pos_name: {self.pos_name}
        technique_id: {self.technique_id}
        technique_name: {self.technique_name}
        body_id: {self.body_id}
        body_name: {self.body_name}
        outcome_id: {self.outcome_id}
        outcome_name: {self.outcome_name}
        """

class FreezeFrame:
    def __init__(self, id, match_id, season, competition, loc_x, loc_y, player, teammate):
        self.id = id
        self.match_id = match_id
        self.season = season
        self.competition = competition
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.player = player
        self.teammate = teammate
    def toString(self):
        return f"""
        id: {self.id}
        match_id: {self.match_id}
        season: {self.season}
        competition: {self.competition}
        loc_x: {self.loc_x}
        loc_y: {self.loc_y}
        player: {self.player}
        teammate: {self.teammate}
        """
