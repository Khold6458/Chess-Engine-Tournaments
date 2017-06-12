# TournamentMaster
A Python CLI for running tournaments between chess engines.

## Installation
`pip install TournamentMaster`

Requires Python3.3+

## Usage
Run a 8-game match between Stockfish and Komodo, with time control 2 minutes
plus 500 milliseconds per move, and save the games to a PGN file.  
`tm new --pgn /path/to/output/pgn --time 120 --inc 500 --rounds 8 Stockfish Komodo`

Generate 16 opening lines by weighted choice from the configured opening book,
saving the output to a PGN file.  
`tm openings -n 16 /path/to/output/pgn`

See more options for running engine tournaments.  
`tm new --help`

## License
`TournamentMaster` is licensed under the GPLv3. See LICENSE.
