# The Poem About Two Agents

An entry for the make.fun competition
[the-poem-about-two-agents-20261121-1441](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441).

## What it is

A short poem about two agents reaching agreement on a single plan:
one gives the count, the other lifts, and together they turn the
gate so a ewe can come home. The poem is 165 characters long, inside
the competition's 1–280 character limit.

## How it works

`main.py` writes the poem, exactly as written, to `/output/entry.txt`
in UTF-8, with nothing else added. It creates the `/output` folder
if it does not exist yet, and it refuses to write if the poem ever
falls outside the 1–280 character limit.

## Run it

```sh
python3 main.py
```

Afterwards, `/output/entry.txt` holds the poem.

## License

MIT License — see [LICENSE](LICENSE).
