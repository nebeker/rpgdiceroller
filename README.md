# rpgdiceroller

Just a basic utility to roll dice for tabletop RPGs.

`rolld(faces)` rolls a `faces`-sided die.

For regular D&D play, run `rolld(20)`. It just rolls off the tounge, doesn't it?

To roll with advantage, `rollad(20)` or with disadvantage, `rolldis(20)`.

To roll with a modifier, `rollmod(faces, mod)`.

Also runs as a flask web app: `app.py`