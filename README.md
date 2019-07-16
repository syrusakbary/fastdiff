# fastdiff

`fastdiff` is a re-implementation of difflib in pure Rust compiled to WebAssembly to speedup different language integrations:

* [Python](https://github.com/syrusakbary/fastdiff/tree/master/python): via [Wasmer](https://github.com/wasmerio/python-ext-wasm), falling back to `difflib` [compare](https://docs.python.org/3/library/difflib.html#difflib.Differ.compare).


## Install

### Python
To install `fastdiff` in Python, you just need to do:

```shell
pip install fastdiff
```

And then, use it in Python like this:
```python
from fastdiff import compare

str1 = 'hello\nwasm\n'
str2 = 'hello\npython\n'

print(compare(str1, str2))
```

## Benchmarks

### Python

When comparing strings with 300 lines, the WebAssembly based approach is about **75 times faster** than the pure Python approach.

```
------------------------------------------------------------------------------------------------ benchmark: 2 tests ------------------------------------------------------------------------------------------------
Name (time in ms)                         Min                    Max                   Mean              StdDev                 Median                 IQR            Outliers     OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_benchmark_content_native        147.7818 (1.0)         152.6777 (1.0)         150.7455 (1.0)        1.5634 (1.0)         151.1331 (1.0)        1.4871 (1.0)           2;1  6.6337 (1.0)           7           1
test_benchmark_content_base       11,171.8288 (75.60)    12,273.8719 (80.39)    11,718.6702 (77.74)    420.9887 (269.27)   11,811.1409 (78.15)    590.1666 (396.86)        2;0  0.0853 (0.01)          5           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

## Building

For building the WebAssembly file, you need Rust and the `wasm32` target.

```
# Install Rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Add wasm32 target
rustup target add wasm32-unknown-unknown
```

And then, run:

```
make build
```

## Testing

For testing in Python you can do:

```
make test_python
```
