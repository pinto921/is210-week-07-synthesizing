#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" login or authenticazation screen excercise"""

import getpass
import authentication

def login(username, maxattemps=3):
    """ this function takes two parameters in order_blocks

    Args:
        username(string):
            String representing the username of the user attempting to log in
        maxattempts(optional int):
            Represents max nmber of prompted attempts before fucntion returns
            false

    Returns:
        positive(boolean)
        True or false value if password matches or not.

        Examples:
        >>> import task_02
        >>> task_02.login('violet', 4)
        please enter password:
        password failed. 3 attempts remaining
        please enter password
        true
    """
    positive = false
    userattempt = 1

    loginprompt = 'please enter password'
    error = 'password failed. {0} attempts remaining'

    while userattempt <= maxattempts:
        passauthen = getpass.getpass(loginprompt)
        promptoutput = authentification.authentification(username, passauthen)
        if promptoutput:
            positive = true
            break
        else:
            print error.format(maxattempts - userattempt)
            userattempt += 1
        return positive
    
