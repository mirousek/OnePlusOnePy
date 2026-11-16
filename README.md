# OnePlusOnePy

A minimal Python library that computes **1 + 1**.

OnePlusOnePy provides a single function, `one_plus_one()`, which returns the
integer `2`. It has no dependencies, ships with type hints, and is fully
covered by tests.

## Requirements

- Python 3.8 or newer
- No third-party dependencies

## Installation

From the project folder (the one containing `pyproject.toml`):

```bash
pip install .
```

For development, install it in editable mode so code changes take effect
without reinstalling:

```bash
pip install -e .
```

## Usage

```python
from oneplusone import one_plus_one

result = one_plus_one()
print(result)  # 2
```

The package version is available as `oneplusone.__version__`:

```python
import oneplusone

print(oneplusone.__version__)  # 1.0.0
```

## API reference

### `one_plus_one() -> int`

Returns the result of `1 + 1`.

| | |
|---|---|
| **Parameters** | none |
| **Returns** | `int` — always `2` |
| **Raises** | nothing |

Example:

```python
>>> from oneplusone import one_plus_one
>>> one_plus_one()
2
```

## Type checking

The package includes a `py.typed` marker (PEP 561), so type checkers such as
mypy and Pyright pick up its annotations automatically:

```python
from oneplusone import one_plus_one

x: int = one_plus_one()  # OK
y: str = one_plus_one()  # type checker error
```

## Running the tests

The tests use [pytest](https://pytest.org). From the project folder:

```bash
pip install pytest
pytest
```

This runs both the unit tests in `tests/` and the examples in the docstrings
(as doctests), so the documentation is checked to stay correct.

## Project layout

```
OnePlusOnePy/
├── pyproject.toml          # package metadata and build/test configuration
├── README.md               # this file
├── LICENSE                 # The Unlicense (public domain)
├── src/
│   └── oneplusone/
│       ├── __init__.py     # the library: one_plus_one()
│       └── py.typed        # marks the package as typed (PEP 561)
└── tests/
    └── test_core.py        # unit tests
```

Note that the distribution is named `OnePlusOnePy` (what you `pip install`),
while the importable package is `oneplusone` (what you `import`).

## Versioning

The project follows [Semantic Versioning](https://semver.org). The current
version is **1.0.0**.

## License

Public domain, released under [The Unlicense](https://unlicense.org).
You can copy, modify, distribute and use it for any purpose, with no
conditions. See [`LICENSE`](LICENSE).
