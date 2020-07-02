# A script to test the  number_of_tieless_games function is working as expected.
# Compares the output to the sequences published on the OEIS.

from tieless_games import number_of_tieless_games

def test_rugby_union():
    first_ten_terms =\
    [1, 6, 30, 180, 1002, 6012, 34224, 205344, 1180010, 7080060]
    # As per the sequence I published: https://oeis.org/A334288
    scoring_events = (-7,-5,-3,3,5,7)
    output = number_of_tieless_games(scoring_events, 9)
    assert first_ten_terms == output

def test_american_football():
    first_ten_terms =\
    [1, 10, 90, 882, 8474, 82650, 803894, 7858034, 76833498, 752970088]
    # As per the sequence: https://oeis.org/A137684
    scoring_events = {2,3,6,7,8,-2,-3,-6,-7,-8}
    output = number_of_tieless_games(scoring_events, 9)
    assert first_ten_terms == output

def test_basketball():
    first_ten_terms =\
    [1, 6, 30, 162, 886, 4932, 27714, 157018, 894942, 5126268]
    # As per the sequence: https://oeis.org/A137684
    scoring_events = [1,2,3,-1,-2,-3]
    output = number_of_tieless_games(scoring_events, 9)
    assert first_ten_terms == output

def test_basketball_without_3_point_line():
    # During the years 1896-1967 basketball had scoring_events = {1, 2, -1, -2}
    first_ten_terms =\
    [1, 4, 12, 42, 148, 540, 1990, 7434, 27972, 106008]
    # As per the sequence: https://oeis.org/A137684
    scoring_events = [1,2,-1,-2]
    output = number_of_tieless_games(scoring_events, 9)
    assert first_ten_terms == output

def test_binary_game():
    first_ten_terms =\
    [1, 2, 2, 4, 6, 12, 20, 40, 70, 140]
    scoring_events = [1,-1]
    output = number_of_tieless_games(scoring_events, 9)
    assert first_ten_terms == output
