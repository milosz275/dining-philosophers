# Dining philosophers

The dining philosophers problem simulation implemented as PyPi package.
- [Repo](https://github.com/mldxo/dining-philosophers)
- [Pypi](https://pypi.org/project/dining-philosophers)

## Usage

In order to build and use the package, you need to have Python 3.8 or higher installed.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Results

After running the simulation, as the output you will see generated image representing 5 philosophers. Each philosopher's time is represented by a line connected with circles that denotes eating time. The line is colored in the philosopher's color. Empty bits represent thinking time. Red triangles represent situation where eating is not possible due to the lack of forks. The simulation is run for 100 seconds.

## License
[MIT](LICENSE)

## Authors
- [ZaumNort](https://github.com/ZaumNort)
- [mldxo](https://github.com/mldxo)
