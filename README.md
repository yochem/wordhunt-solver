# Word Hunt / Boggle Solver

Frustrated that a certain word hunt implementation requires _Premium_ to view
the longest words afterwards, I wrote this solver in the middle of a random
night.

Small (~100 LOC) solver for the Word Hunt (or _Boggle_) game. The solver is
written in Python and can find all possible words in the game in ~0.002
seconds (2 ms).

The solver recursively walks the board, continuously checking if its path can
lead to a valid word. It uses `/usr/share/dict/words` as word list.

## Example

```
$ python3 wordhunt.py
>>> Grid (4x4):
acto
snte
rmhm
iain

Found 133 words in 0.0015 seconds

Words with 8 characters:
anthemia

Words with 6 characters:
ahimsa
anhima
anthem
mehari

Words with 5 characters:
ahmet
canto
...
```

## Requirements

`None`. Probably a not-outdated Python version. Oh yeah, and a word list.

## License

Public domain.
