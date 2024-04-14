CREATE TABLE countries (
    name VARCHAR(255) PRIMARY KEY,
    id INT UNIQUE NOT NULL
);

CREATE TABLE competitions (
    name VARCHAR(255) PRIMARY KEY,
	id INT UNIQUE NOT NULL,
    country VARCHAR(255) NOT NULL,
    gender VARCHAR(255),
    youth BOOLEAN,
    international BOOLEAN,
	FOREIGN KEY (country)
    	REFERENCES countries (name)
);

CREATE TABLE managers (
    name VARCHAR(255) PRIMARY KEY,
    id INT UNIQUE NOT NULL,
    nickname VARCHAR(255),
    dob DATE,
    country VARCHAR(255) NOT NULL,
    FOREIGN KEY (country)
    	REFERENCES countries (name)
);

CREATE TABLE teams (
    name VARCHAR(255) PRIMARY KEY,
    id INT UNIQUE NOT NULL,
    gender VARCHAR(255),
    grp VARCHAR(255),
    country VARCHAR(255) NOT NULL,
    manager VARCHAR(255),
    FOREIGN KEY (country)
    	REFERENCES countries (name),
    FOREIGN KEY (manager)
    	REFERENCES managers (name)
);

CREATE TABLE stadiums (
    name VARCHAR(255) PRIMARY KEY,
    id INT UNIQUE NOT NULL,
    country VARCHAR(255) NOT NULL,
    FOREIGN KEY (country)
    	REFERENCES countries (name)
);

CREATE TABLE referees (
    name VARCHAR(255) PRIMARY KEY,
    id INT UNIQUE NOT NULL,
    country VARCHAR(255) NOT NULL,
    FOREIGN KEY (country)
    	REFERENCES countries (name)
);

CREATE TABLE matches (
    id INT PRIMARY KEY,
    season VARCHAR(255) NOT NULL,
	competition VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    kick_off TIME NOT NULL,
    home_team VARCHAR(255) NOT NULL,
    away_team VARCHAR(255) NOT NULL,
    home_score INT NOT NULL,
    away_score INT NOT NULL,
    week INT,
    competition_stage VARCHAR(255),
    stadium VARCHAR(255),
    referee VARCHAR(255),
	FOREIGN KEY (competition)
		REFERENCES competitions (name),
    FOREIGN KEY (home_team)
    	REFERENCES teams (name),
    FOREIGN KEY (away_team)
    	REFERENCES teams (name),
    FOREIGN KEY (stadium)
    	REFERENCES stadiums (name),
    FOREIGN KEY (referee)
    	REFERENCES referees (name)
);

CREATE TABLE formations (
    event_id VARCHAR(255) PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255), 
    formation VARCHAR(255),
    FOREIGN KEY (team)
        REFERENCES teams (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id)
);

CREATE TABLE players (
    name VARCHAR(255) PRIMARY KEY,
    id INT UNIQUE NOT NULL,
    jersey INT,
    team VARCHAR(255),
    country VARCHAR(255),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (country)
    	REFERENCES countries (name)
);

CREATE TABLE lineups (
    match_id INT NOT NULL,
    season VARCHAR(255) NOT NULL,
    competition VARCHAR(255) NOT NULL,
    team VARCHAR(255) NOT NULL,
    player VARCHAR(255) NOT NULL
);

CREATE TABLE cards (
    player VARCHAR(255),
    match_id INT NOT NULL,
    season VARCHAR(255) NOT NULL,
    competition VARCHAR(255) NOT NULL,
    time VARCHAR(255),
    card_type VARCHAR(255),
    reason VARCHAR(255),
    period INT
);

CREATE TABLE positions (
    match_id INT NOT NULL,
    season VARCHAR(255) NOT NULL,
    competition VARCHAR(255) NOT NULL,
    player VARCHAR(255) NOT NULL,
    position_id INT NOT NULL,
    position VARCHAR(255) NOT NULL,
    from_time VARCHAR(255),
    to_time VARCHAR(255),
    from_period INT,
    to_period INT,
    start_reason VARCHAR(255),
    end_reason VARCHAR(255)
);

CREATE TABLE events (
    id VARCHAR(255),
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    indx INT,
    period INT,
    timestamp TIME,
    minute INT,
    second INT,
    team VARCHAR(255),
    player VARCHAR(255),
    type_id INT,
    type_name VARCHAR(255),
    possession INT,
    possession_team VARCHAR(255),
    pattern_id INT,
    pattern_name VARCHAR(255),
    loc_x FLOAT,
    loc_y FLOAT,
    duration FLOAT,
    counterattack BOOLEAN,
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name),
    FOREIGN KEY (possession_team)
        REFERENCES teams (name)
) PARTITION BY LIST (season);
CREATE TABLE EVENTS_PL_2003_2004 PARTITION OF events FOR VALUES IN ('2003/2004');
CREATE TABLE EVENTS_LL_2018_2019 PARTITION OF events FOR VALUES IN ('2018/2019');
CREATE TABLE EVENTS_LL_2019_2020 PARTITION OF events FOR VALUES IN ('2019/2020');
CREATE TABLE EVENTS_LL_2020_2021 PARTITION OF events FOR VALUES IN ('2020/2021') PARTITION BY LIST(type_name);
    CREATE TABLE LL_2020_2021_DP PARTITION OF EVENTS_LL_2020_2021 FOR VALUES IN ('Dribbled Past');
    CREATE TABLE LL_2020_2021_REST PARTITION OF EVENTS_LL_2020_2021 DEFAULT;

CREATE TABLE shots (
    event_id VARCHAR(255),
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    statsbomb_xg FLOAT,
    loc_x FLOAT,
    loc_y FLOAT,
    loc_z FLOAT,
    follows_dribble BOOLEAN,
    first_time BOOLEAN,
    open_net BOOLEAN,
    deflected BOOLEAN,
    technique_id INT,
    technique_name VARCHAR(255),
    body_id INT,
    body_name VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name)
) PARTITION BY LIST (season);
CREATE TABLE SHOTS_PL_2003_2004 PARTITION OF shots FOR VALUES IN ('2003/2004');
CREATE TABLE SHOTS_LL_2018_2019 PARTITION OF shots FOR VALUES IN ('2018/2019') PARTITION BY LIST(first_time);
    CREATE TABLE LL_2018_2019_FT PARTITION OF SHOTS_LL_2018_2019 FOR VALUES IN (TRUE);
    CREATE TABLE LL_2018_2019_FT_REST PARTITION OF SHOTS_LL_2018_2019 DEFAULT;
CREATE TABLE SHOTS_LL_2019_2020 PARTITION OF shots FOR VALUES IN ('2019/2020') PARTITION BY LIST(first_time);
    CREATE TABLE LL_2019_2020_FT PARTITION OF SHOTS_LL_2019_2020 FOR VALUES IN (TRUE);
    CREATE TABLE LL_2019_2020_FT_REST PARTITION OF SHOTS_LL_2019_2020 DEFAULT;
CREATE TABLE SHOTS_LL_2020_2021 PARTITION OF shots FOR VALUES IN ('2020/2021') PARTITION BY LIST(first_time);
    CREATE TABLE LL_2020_2021_FT PARTITION OF SHOTS_LL_2020_2021 FOR VALUES IN (TRUE);
    CREATE TABLE LL_2020_2021_FT_REST PARTITION OF SHOTS_LL_2020_2021 DEFAULT;

CREATE TABLE passes (
    event_id VARCHAR(255),
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    recipient VARCHAR(255),
    length FLOAT,
    angle FLOAT,
    height_id INT,
    height_name VARCHAR(255),
    aerial_won BOOLEAN,
    loc_x FLOAT,
    loc_y FLOAT,
    assisted_shot_id VARCHAR(255),
    deflected BOOLEAN,
    miscomm BOOLEAN,
    crossed BOOLEAN,
    cut_back BOOLEAN,
    switch BOOLEAN,
    shot_assist BOOLEAN,
    goal_assist BOOLEAN,
    body_id INT,
    body_name VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    technique_id INT,
    technique_name VARCHAR(255),  
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name),
    FOREIGN KEY (recipient)
    	REFERENCES players (name)
) PARTITION BY LIST (season);
CREATE TABLE PASSES_PL_2003_2004 PARTITION OF passes FOR VALUES IN ('2003/2004');
CREATE TABLE PASSES_LL_2018_2019 PARTITION OF passes FOR VALUES IN ('2018/2019');
CREATE TABLE PASSES_LL_2019_2020 PARTITION OF passes FOR VALUES IN ('2019/2020');
CREATE TABLE PASSES_LL_2020_2021 PARTITION OF passes FOR VALUES IN ('2020/2021') PARTITION BY LIST (technique_name);
    CREATE TABLE LL_2020_2021_THRUBALL PARTITION OF PASSES_LL_2020_2021 FOR VALUES IN ('Through Ball');
    CREATE TABLE LL_2020_2021_OTHERPASSES PARTITION OF PASSES_LL_2020_2021 DEFAULT;
CREATE INDEX idx_season_team ON passes (season, team);


CREATE TABLE bad_behaviours (
    event_id VARCHAR(255) PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    card_id INT, 
    card_name VARCHAR(255),
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name)
);

CREATE TABLE fouls (
    event_id VARCHAR(255) PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    offensive BOOLEAN,
    foul_id INT,
    foul_name VARCHAR(255),
    advantage BOOLEAN,
    penalty BOOLEAN,
    card_id INT,
    card_name VARCHAR(255),
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name)
);

CREATE TABLE fouls_won (
    event_id VARCHAR(255) PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    defensive BOOLEAN,
    advantage BOOLEAN,
    penalty BOOLEAN,
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name)
);

CREATE TABLE dribbles (
    event_id VARCHAR(255),
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    overrun BOOLEAN,
    nutmeg BOOLEAN,
    outcome_id INT,
    outcome_name VARCHAR(255),
    no_touch BOOLEAN,
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name)
) PARTITION BY LIST (season);
CREATE TABLE DRIBBLES_LL PARTITION OF dribbles FOR VALUES IN ('2018/2019', '2019/2020', '2020/2021') PARTITION BY LIST (outcome_name);
    CREATE TABLE DRIBBLES_LL_COMPLETE PARTITION OF DRIBBLES_LL FOR VALUES IN ('Complete');
    CREATE TABLE DRIBBLES_LL_REST PARTITION OF DRIBBLES_LL DEFAULT;
CREATE TABLE DRIBBLES_PL PARTITION OF dribbles FOR VALUES IN ('2003/2004');

CREATE TABLE ball_recoveries (
    event_id VARCHAR(255) PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    offensive BOOLEAN,
    failure BOOLEAN,
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name)
);

CREATE TABLE ball_receipts (
    event_id VARCHAR(255) PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name)
);

CREATE TABLE carries (
    event_id VARCHAR(255) PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    loc_x FLOAT, 
    loc_y FLOAT,
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name)
);

CREATE TABLE blocks (
    event_id VARCHAR(255) PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    deflection BOOLEAN,
    offensive BOOLEAN,
    save BOOLEAN,
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name)
);

CREATE TABLE duels (
    event_id VARCHAR(255) PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name)
);

CREATE TABLE clearances (
    event_id VARCHAR(255) PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    aerial_won BOOLEAN,
    body_id INT,
    body_name VARCHAR(255),
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name)
);

CREATE TABLE substitutions (
    event_id VARCHAR(255) PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    subbed_name VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name),
    FOREIGN KEY (subbed_name)
    	REFERENCES players (name)
);

CREATE TABLE interceptions (
    event_id VARCHAR(255) PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name)
);

CREATE TABLE goalkeepers (
    event_id VARCHAR(255) PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    team VARCHAR(255),
    player VARCHAR(255),
    pos_id INT,
    pos_name VARCHAR(255),
    technique_id INT,
    technique_name VARCHAR(255),
    body_id INT,
    body_name VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (team)
    	REFERENCES teams (name),
    FOREIGN KEY (player)
    	REFERENCES players (name)
);

CREATE TABLE freeze_frames (
    id VARCHAR(255),
    match_id INT NOT NULL,
    season varchar(255) NOT NULL,
    competition varchar(255) NOT NULL,
    loc_x FLOAT,
    loc_y FLOAT,
    player VARCHAR(255),
    teammate BOOLEAN,
    FOREIGN KEY (competition)
        REFERENCES competitions (name),
    FOREIGN KEY (match_id)
        REFERENCES matches (id),
    FOREIGN KEY (player)
    	REFERENCES players (name)
);