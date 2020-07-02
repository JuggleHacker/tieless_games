# tieless_games
Code to calculate the number of possible tieless games for a range of sports.
A game is a sequence of scores (positive for the home team, negative for the visiting team).
For example, in Rugby union, a scoring event can be worth 3 (penalty/kick), 5 (unconverted try) or 7 (converted try).
An example game with three scoring events would be (-7, 5, -3). 
Note the score is never tied, except at the start when neither team has scored. This means it is a tieless game.
This project is concerned with calculating the number of tieless games with a given number of scoring events.
This code was used to generate the terms of the sequence which I published in the OEIS:
https://oeis.org/A334288

