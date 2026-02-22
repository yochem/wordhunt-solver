# Word Hunt / Boggle Solver


<img height="300px" src="https://private-user-images.githubusercontent.com/23235841/553257112-50f798fc-0072-46e7-9288-2397fc2c4f9c.jpg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzE3OTYxMDMsIm5iZiI6MTc3MTc5NTgwMywicGF0aCI6Ii8yMzIzNTg0MS81NTMyNTcxMTItNTBmNzk4ZmMtMDA3Mi00NmU3LTkyODgtMjM5N2ZjMmM0ZjljLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAyMjIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMjIyVDIxMzAwM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTcyNTk0NmU2MGVhYjVhMzQ3OTcwYjhhYmFmNmI2MTE4MjFlNjljYTNmOWEyZWI2YjZkMzQ2YjU3ZDM4NGM5MWImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.16deU5UuKJPyaos5CoP06CS-3h7R8_BWxr6PVv5kx4g"></img>

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
