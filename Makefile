
build:
	cargo build --manifest-path wasm/Cargo.toml --release --target=wasm32-unknown-unknown
	cp wasm/target/wasm32-unknown-unknown/release/fastdiff.wasm fastdiff.wasm

optimize:
	wasm-strip fastdiff.wasm
	wasm-opt -O3 fastdiff.wasm -o fastdiff.wasm

test_python: python
	cd python && pytest -s --benchmark-skip

test: test_python

bench_python: python
	cd python && pytest --benchmark-only

bench: bench_python

all: build optimize test_python

python: build optimize
	cp fastdiff.wasm python/fastdiff/

publish:
	cd python && python setup.py sdist bdist_wheel
	cd python && python setup.py sdist upload
