# Fastdiff

Fastdiff is a re-implementation of difflib in pure Rust compiled to WebAssembly to speedup different language integrations:

* Python: via [Wasmer](https://github.com/wasmerio/python-ext-wasm), falling back to `difflib` [compare](https://docs.python.org/3/library/difflib.html#difflib.Differ.compare).

## Benchmarks

### Python

When comparing strings with 300 lines, the WebAssembly based approach is about **75 times faster** than the pure Python approach.

```
------------------------------------------------------------------------------------------------ benchmark: 2 tests ------------------------------------------------------------------------------------------------
Name (time in ms)                         Min                    Max                   Mean              StdDev                 Median                 IQR            Outliers     OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_benchmark_content_native        137.9896 (1.0)         145.8701 (1.0)         141.2983 (1.0)        2.8708 (1.0)         140.5982 (1.0)        4.2806 (1.0)           3;0  7.0772 (1.0)           7           1
test_benchmark_content_base       10,665.8390 (77.29)    11,141.3282 (76.38)    10,837.7984 (76.70)    183.8493 (64.04)    10,817.5194 (76.94)    206.9630 (48.35)         1;0  0.0923 (0.01)          5           1
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
