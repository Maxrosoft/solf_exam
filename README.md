# solf_exam

solf_exam is a Python project which can help you if you are going to pass your solfeggio exam at the 8-th grade of musical school in Ukraine.

## Usage

major

```python
gamma = Gamma() 
"""
if there are no arguments, 
then a natural C major is created
"""
gamma.to_chromatic("major") 
print(gamma.get_gamma())
```