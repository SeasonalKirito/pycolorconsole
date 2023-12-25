# PyColorConsole 🌈

PyColorConsole is a simple Python package that provides a convenient way to add colored text to your console output. It includes a `ColorPalette` class with predefined color codes and functions for logging colored text.

## Installation 📩

You can install PyColorConsole using pip:

```bash
pip install git+https://github.com/pycolorconsole/pycolorconsole.git
```

## Usage 🎨

### ColorPalette

The `ColorPalette` class provides predefined color codes for use in your console output:

- `WHITE = "\033[37m"`
- `BLACK = "\033[30m"`
- `RED = "\033[31m"`
- `GREEN = "\033[32m"`
- `YELLOW = "\033[33m"`
- `BLUE = "\033[34m"`
- `MAGENTA = "\033[35m"`
- `CYAN = "\033[36m"`

### Functions

#### `init(autoReset: bool)`

Initialize the color console with an option to automatically reset colors after each use.

Example:
```python
from pycolorconsole.create import init

# Set autoReset to False to disable automatic color reset
init(autoReset=False)
```

#### `log(color=ColorPalette.WHITE, text="returned None")`

Log colored text to the console.

Parameters:
- `color`: Color code from `ColorPalette` (default is `ColorPalette.WHITE`)
- `text`: Text to be logged (default is `"returned None"`)

Example:
```python
from pycolorconsole.create import log, ColorPalette

# Log red text
print(log(ColorPalette.RED, "Error: Something went wrong!"))
```