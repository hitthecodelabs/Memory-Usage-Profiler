# Memory-Usage-Profiler

This repository contains a Python script designed for monitoring the sizes of variables in memory, especially tailored for environments like Google Colab or Jupyter Notebooks.

## Overview

The script provides functions to list variables along with their memory sizes in a human-readable format. This can be particularly useful in data-intensive environments where efficient memory management is crucial.

## Features

- **Human-Readable Format**: Converts byte sizes into a more readable format (e.g., KB, MB).
- **Size Calculation**: Calculates the size of variables, including nested structures like lists, dictionaries, and custom objects.
- **Top N Variables**: Lists the top N variables consuming the most memory.
- **Pandas DataFrame Output**: Displays the results in a structured and readable table using Pandas DataFrame.

## Usage

To use the script, simply import it into your Python environment and call the `list_variables_size` function. 

```python
import memory_monitor

# List top 10 variables by size
memory_monitor.list_variables_size()
```

You can adjust the number of variables displayed by passing a different number to the function.

## Requirements

- Python 3.x
- Pandas

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
