"""
Hash visualization tool inspired by beautiful ssh-keygen randomart.

Typical usage as CLI::

    $ hashime -f LICENSE
    +----[LICENSE]----+
    |    ..o +        |
    |   o E.= o       |
    |  o +.. o        |
    | . o o.o         |
    |.   o =.S.       |
    |..   o.+..+      |
    |o.  o.oo+..=     |
    |. . *+=..+o o .  |
    |  .=+O.++  . o.. |
    +-----[SHA256]----+

Typical usage in code::

    >>> import hashime
    >>> digest = hashime.file_digest('./LICENSE')
    >>> art = hashime.drunken_bishop(digest)
    >>> framed = hashime.frame(art, top_text='LICENSE', bottom_text='SHA256')
    >>> print(framed)
    +----[LICENSE]----+
    |    ..o +        |
    |   o E.= o       |
    |  o +.. o        |
    | . o o.o         |
    |.   o =.S.       |
    |..   o.+..+      |
    |o.  o.oo+..=     |
    |. . *+=..+o o .  |
    |  .=+O.++  . o.. |
    +-----[SHA256]----+
"""
from hashime.drunken_bishop import drunken_bishop
from hashime.fish_tank import fish_tank
from hashime.util import file_digest, frame

__all__ = ['drunken_bishop', 'fish_tank', 'file_digest', 'frame']
