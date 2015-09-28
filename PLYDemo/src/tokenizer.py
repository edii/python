"""DO NOT REMOVE THIS HEADER

BSD License: http://www.opensource.org/licenses/bsd-license.php

Copyright (c) 2008, Sun Microsystems, Inc
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1.Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2.Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation and/or
 other materials provided with the distribution.

3.Neither the name of the Sun Microsystems, Inc nor the names of its contributors may
be used to endorse or promote products derived from this software without
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
# tokenizer.py
#
# A simple symbol recognizer using PLY (http://www.dabeaz.com/ply/)
#
# To run this sample, you will need have 'PLY' installed. Please see the README
# file (in the Files browser)
#

# Use Case: Enter a line of text, and for each symbol, is printed- whether
# it is a Digit/Number, a Lower Case letter or an Upper Case letter, or Other
#
# Actually the use case only makes use of 'lex.py' i.e the lexer part of the
# package


import sys
import ply.lex as lex


__author__ = "Amit Saha <amitksaha@netbeans.org>"
__date__ = "$29 Nov, 2008 10:13:07 PM$"


# Token List
tokens = (
    'DIGIT',
    'LOWERCASELETTER',
    'UPPERCASELETTER',
    'OTHER',
    )

# Regular Expressions for the tokens
t_DIGIT = r'\d+'
t_LOWERCASELETTER = r'[a-z]'
t_UPPERCASELETTER = r'[A-Z]'
t_OTHER = r'[^0-9^a-z^A-Z]'

# Build the lexer
lex.lex()


# Error handling rule
# We really do not need error handling here. In this trivial case, we have
# accounted for all the undesired characters in the OTHER category
# Ignore the warning..
# For details: Please see the Ply documentation

# Process input and tokenize
while 1:
    input = raw_input("Pressing 'X' anywhere in the input will cause an exit\n >>") # Take user inputs

    # Extract each symbol and feed it into the character
    
    for symbol in input:

        if symbol <> 'X':

            lex.input(symbol) # feed each symbol into the lexer
            tok = lex.token()
            if not tok: break
            print tok.type # print only the token type

        else:
            # EXIT
            sys.exit(0)