#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" players data excercise"""

def get_matches(players):
    """ this function takes a list of players and produces unique matchups between players stored as a list of tuple

    Args:
        players(list): list of players that need to be processed

    Returns:
        output:(list):list of tuples containing the matchups

    Examples:
        >>> import task_01
        >>> task_01.get_matches(['Harry', 'Howard', 'Hugh')]

        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]

    """
    output = []

    for index1, item1 in enumerate(players):
        for index2, item2 in enumerate(players):
            if item1 is not item2 and index1 < index2:
                output.append ((item1,item2))
            else:
                continue
        return output
    
