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
------------------------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------------------------
Name (time in ms)                         Min                    Max                   Mean              StdDev                 Median                 IQR            Outliers      OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_benchmark_content_native        217.7005 (2.37)        238.4103 (2.19)        228.3585 (2.36)       9.6103 (1.90)        228.7163 (2.41)      18.3672 (3.93)          2;0   4.3791 (0.42)          5           1
test_benchmark_content_base       12,544.6881 (136.31)   12,869.7072 (118.48)   12,694.1878 (130.98)   116.3574 (22.97)    12,686.6452 (133.48)   110.7123 (23.70)         2;0   0.0788 (0.01)          5           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
