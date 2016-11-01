-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


create database tournament;
\c tournament;

-- look up DROP IF EXISTS if needed


create table players (
	player_id	serial		primary key,
	name		text
);

create table matches (
	match_id	serial		primary key,
	player1		integer 	references players (player_id),
	player2		integer 	references players (player_id),
	winner		integer,
	loser		integer
);