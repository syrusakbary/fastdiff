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

When comparing strings with 300 lines, the WebAssembly based approach is about **100 times faster** than the pure Python approach.

```
---------------------------------------------------------------------------------------------- benchmark: 3 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                        Min                   Max                  Mean             StdDev                Median                IQR            Outliers      OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_benchmark_content_native        47.0735 (1.0)         50.7082 (1.0)         47.4401 (1.0)       0.7944 (1.0)         47.1680 (1.0)       0.2133 (1.0)           2;2  21.0792 (1.0)          21           1
test_benchmark_compile_native     1,187.2395 (25.22)    1,305.0581 (25.74)    1,222.2197 (25.76)    48.3778 (60.90)    1,198.9380 (25.42)    51.4950 (241.44)        1;0   0.8182 (0.04)          5           1
test_benchmark_content_base       5,480.3568 (116.42)   5,623.0508 (110.89)   5,516.5008 (116.28)   60.7623 (76.49)    5,487.1852 (116.33)   57.0271 (267.38)        1;0   0.1813 (0.01)          5           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
