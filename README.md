# PyColorConsole 🌈

PyColorConsole is a simple Python package that provides a convenient way to add colored text to your console output. It includes a `Fore` class with predefined color codes and functions for logging colored text.

## Installation 📩

You can install PyColorConsole using pip:

```bash
pip install git+https://github.com/SeasonalKirito/pycolorconsole.git
```

## Usage 🎨

### Fore

The `Fore` class provides predefined color codes for use in your console output:

- RESET           = 0
- 
- BLACK           = 30
- RED             = 31
- GREEN           = 32
- YELLOW          = 33
- BLUE            = 34
- MAGENTA         = 35
- CYAN            = 36
- WHITE           = 37
- 
- LIGHTBLACK      = 90
- LIGHTRED        = 91
- LIGHTGREEN      = 92
- LIGHTYELLOW     = 93
- LIGHTBLUE       = 94
- LIGHTMAGENTA    = 95
- LIGHTCYAN       = 96
- LIGHTWHITE      = 97

### Functions

#### `init(autoReset: bool)`

Initialize the color console with an option to automatically reset colors after each use.

Example:
```python
from pycolorconsole import init

# Set autoReset to False to disable automatic color reset
init(autoReset=False)
```

#### `log(color=Fore.WHITE, text="returned None")`

Log colored text to the console.

Parameters:
- `color`: Color code from `Fore` (default is `Fore.WHITE`)
- `text`: Text to be logged (default is `"returned None"`)

Example:
```python
from pycolorconsole import log, Fore

# Log red text
print(log(Fore.RED, "Error: Something went wrong!"))
```
