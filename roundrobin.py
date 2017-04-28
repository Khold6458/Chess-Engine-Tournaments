#! /usr/bin/env python
#
# This file is part of TournamentMaster.
# Copyright (C) 2017  Simon Chen
#
# TournamentMaster is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TournamentMaster is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TournamentMaster. If not, see <http://www.gnu.org/licenses/>.

from collections import deque

# The scheduling algorithm used is a carousel where all boards are
# flipped after every round. This has flaws in color distribution.
# If color distribution is very important, run an even number of rounds.


def new_tournament(players, rounds):
    return RoundRobinTournament(players, rounds)


class RoundRobinTournament():
    def __init__(self, players, rounds):
        self.players = players
        self.rounds = rounds

        self.current_round = 0
        self.index = 0
        self.pairings = []
        self.results = []

    def next_round(self):
        self.current_round += 1
        self.results.append([])
        _players = list(self.players)
        if len(_players) % 2 == 1:
            # We use None to represent a 'bye'
            _players.append(None)

        half_len = len(_players) // 2
        top_half = deque(_players[:half_len], half_len)
        bottom_half = deque(_players[half_len:], half_len)

        for index in range(len(_players) - 1):
            if (index + self.current_round) % 2 == 0:
                self.pairings.extend(zip(top_half, bottom_half))
            else:
                self.pairings.extend(zip(bottom_half, top_half))

            fixed = top_half.popleft()
            top_half.appendleft(bottom_half.popleft())
            bottom_half.append(top_half.pop())
            top_half.appendleft(fixed)

    def update(self, result):
        self.results[-1].append(result)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.pairings[self.index]
        except IndexError:
            if self.current_round >= self.rounds:
                raise StopIteration()
            self.next_round()

        pairing = self.pairings[self.index]
        self.index += 1
        if None in pairing:
            return self.__next__()
        return self.current_round, pairing
