import base64
import hashlib

import hashime
import pytest


def key_to_digest(key: str) -> bytes:
    decoded = base64.standard_b64decode(key)
    hash = hashlib.sha256(decoded)
    return hash.digest()


key1 = 'AAAAC3NzaC1lZDI1NTE5AAAAIGAaC/j/5r5xDP+1fECB0zOS705VV8b41WHy5VMO6Xp2'
art1 = """        o.*+ .   
       + * oo.   
      o = = +    
 .   .   * =     
  o  .  S o.+    
.. ....   oo     
.. E+ ..ooo      
  o.oo oo=oo     
 ..o +*+==+      """

key2 = 'AAAAC3NzaC1lZDI1NTE5AAAAIJWirJiqZR0H2M4h6W9bRVGa3ZbvtGhE5R/V6FIX58Xo'
art2 = """    ..           
   ..            
   ..     .      
  .  .   . o    .
o.o . . S o +.o o
oo *   . o B.=oo+
  . +   + +.Boo=.
   o.o.o . Bo.. o
  .o=Eo.  oo=.   """


@pytest.mark.parametrize('key, art', [(key1, art1), (key2, art2)])
def test_drunken_bishop(key, art):
    digest = key_to_digest(key)
    assert hashime.drunken_bishop(digest) == art
