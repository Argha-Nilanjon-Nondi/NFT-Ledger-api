from lib.Story import Story

signature="5f9dc207c0577846a40cf5c4fecb4b781d7980482e4b6fa62cfb63514be01d581535d59da29a....."

publicKey="""2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d413047......."""

objStory=Story()
print(objStory.check_signature(signature=signature,publicKey=publicKey))