# README

## Note: `random_hostname.py` changes system hostname; be sure user wants system hostname to change.

## Shebang/Interpreter Directive

The **shebang line** starts with `#!`, because those human-readable characters, encoded to ASCII, become **0x23** and **0x21**, which together become a _magic number_ or a magic byte string detected by functions in the [exec()](http://man7.org/linux/man-pages/man3/exec.3.html) family. Such `exec()` functions ascertain whether a file is an executable binary or a script.

**Note**: the space between the _shebang_ and the _interpreter directive_ is optional.

## Import Modules

```python
from random import randrange
from subprocess import run
```

- `random.randrange()` returns a random integer within a specific range.
- `subprocess.run()` executes command line arguments in Bash from Python.

## `rand_host`

An [f-string](https://www.python.org/dev/peps/pep-0498/) is assigned to `rand_host`. Each set of braces contains an embedded expression. For example, the f-string `f'{rand_az()}'` could become `'q'`, since `rand_az()` returns a random lowercase letter.

```python
rand_host = f'{rand_az()}{rand_AZ()}{rand_09()}{rand_az()}{rand_AZ()}{rand_09()}'
```

`rand_host` would contain something akin to `mV4jA8`, as each embedded expression returns a character. See _Example Prompt_ section.

## Example Prompt

```shell
foo@sA1nJ5:~/Desktop $
```
