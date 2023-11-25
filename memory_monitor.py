import sys
import pandas as pd

def sizeof_fmt(num, suffix='B'):
    """
    Convert a byte size into a human-readable format.

    Parameters:
    num (int): Size in bytes.
    suffix (str, optional): Suffix for the size. Default is 'B' (bytes).

    Returns:
    str: Human-readable size.
    """
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix)

def get_size(obj, seen=None):
    """
    Recursively finds size of objects in bytes.

    Parameters:
    obj (object): The object to find the size of.
    seen (set, optional): Set of already processed objects to avoid recursive loops. Default is None.

    Returns:
    int: Size of the object in bytes.
    """
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Mark as seen
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size

def list_variables_size(n=10):
    """
    List top N variables in the local scope sorted by their memory usage.

    Parameters:
    n (int, optional): Number of variables to list. Default is 10.

    Returns:
    DataFrame: Pandas DataFrame with variable names and their sizes.
    """
    local_vars = list(locals().items())
    var_sizes = [(name, get_size(value)) for name, value in local_vars]
    var_df = pd.DataFrame(var_sizes, columns=['Variable', 'Size'])
    var_df.sort_values(by='Size', ascending=False, inplace=True)
    var_df.reset_index(drop=True, inplace=True)
    var_df['Size'] = var_df['Size'].apply(sizeof_fmt)
    return var_df.head(n)

# Example usage:
# list_variables_size()

