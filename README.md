# titration-curve
Perform titration curves of any acid-base pair.

## Dependencies
- python 3+
- matplotlib
- numpy

## Examples

### Titration of weak diprotic-acid with strong base
```python

# define the sample and the titrant species
# first argument: concentration
# second argument: list of pK's (pKa's or pKb's) (optional, default assumes strong acid/base)
# third argument: volume (optional)

sample = Acid(0.5, [4, 7])
titrant = Base(0.5)

# calling the titration function. Returns the titrated fraction array (phi) and the pH array
phi, pH = titrate(sample, titrant)

# ploting the result

plt.plot(phi, pH)

plt.title('Titulação legal!')
plt.xlabel('Fração titulada')
plt.ylabel('pH')
```

### Titration of strong base with strong acid
```python
sample = Base(0.3) # inital concentration of 0.3 mol/L
titrant = Acid(0.5) # inital concentration of 0.5 mol/L

phi, pH = titrate(sample, titrant)

plt.plot(phi, pH)

plt.title('Titulação legal!')
plt.xlabel('Fração titulada')
plt.ylabel('pH')
```