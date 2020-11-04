# README
Repo name: `random_hostname_nick3499`
Set system hostname with pseudo-random alpha-numeric string.

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
- `subprocess.run()` executes Bash command described by args from Python.

## subprocess.run()

After the script is done juggling and playing slight of hand with characters, `rand_host` is passed as an arg to `hostnamectl` through the `subprocess.run()` method.

```python
run(['sudo', 'hostnamectl', 'set-hostname', rand_host], check=True)
```

- `subprocess.run()` runs `hostnamectl` in Bash, waits for `hostnamectl` to finish, then returns a `CompletedProcess` instance.
- `check=True` captures `stdout` or `stderr`.

## random.randrange()

`random.randrange()` returns a peudo-random number. _psuedo_-random, basically, because _random logic_ is an oxymoron. `random.randrange()` takes three integers: **random.randrange(start, stop, increment)**. The integer returned becomes a Unicode code point passed to the [chr()](https://docs.python.org/3/library/functions.html#chr) built-in method, where `chr(97)` returns `'a'`, so `chr(randrange(97, 123, 1))` will return a pseudo-random lowercase letter between `'a'` and `'z'`, just as the f-string `f'{rand_lwr()}'` returns a lowercase letter.

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
[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/R6R72LISM)
