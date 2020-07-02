# A game is a sequence of scores (positive for the home team,
# negative for the visiting team).
# For example, in American football, the set of valid scores is
# {2,3,6,7,8,-2,-3,-6,-7,-8}.
# For rugby, the set of valid scores in {3,5,7,-3,-5,-7}
# A tie-less game is one in which the teams are never in a tie
# (except at the beginning, when no team has scored yet).


def number_of_tieless_games(scoring_events, n):
    """
    Takes in an iterable, scoring_events, containing the possible scores in the
    game. For example, for football, it would be {1,-1}.
    For rugby union, it would be [3,5,7,-3,-5,-7].
    Negative points represent points for the away team, positive points
    represent points for the home team
    Also takes in n, a number of scoring events.
    Returns a list of length n+1 where the ith entry is the number of tieless
    games with i scoring events, where each scoring event is a member of
    scoring_events.
    For example, number_of_tieless_games({1,2,-1,-2},3) returns [1,4,12],
    because there is a unique game with 0 scoring events.
    Any game with 1 scoring event is tieless, and there are 4 of them.
    Of the 16 (4**2) games with 2 scoring events, all apart from
    [2,-2], [-2,2], [-1,1] and [1,-1] are tieless, so there are 12 which are
    tieless.
    """
    dictionary_of_scores = {0:1}
    list_to_return = [1]
    # The keys of this dictionary represent possible scores.
    # The values represent the number of ways this score can be reached with
    # the game being tied at every point.

    for i in range(n):
        # At each stage, we have the non-zero scores with i scoring events in
        # dictionary_of_scores. To find non-zero scores with i+1 scoring events
        # consider each non-zero score, and each possibility for the next
        # scoring event.
        old_dictionary = dictionary_of_scores
        dictionary_of_scores = {}
        for score, number_of_ways in old_dictionary.items():
            for scoring_event in scoring_events:
                new_score = score + scoring_event
                if new_score != 0:
                    dictionary_of_scores[new_score] =\
                    dictionary_of_scores.get(new_score, 0) + number_of_ways
        list_to_return.append(sum(dictionary_of_scores.values()))
    return list_to_return
