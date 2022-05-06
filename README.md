# solf_exam

solf_exam is a Python project which can help you if you are going to pass your solfeggio exam at the 8-th grade of musical school in Ukraine.

## Usage

minor

```python
gamma = Gamma(
    {
        "la": None, "si": None, "do": None, "re": None,
        "mi": None, "fa": None, "sol": None, "la2": None
    }
) # - for example
gamma.to_chromatic("minor")
print(gamma.get_gamma())
```