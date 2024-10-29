# AtomicBenchmark

Benchmark of 20 billion atomic arithmetics in parallel.

- **CPU**: Apple Silicon M3
- **OS**: macOS 15.1

## Benchmark result

| **Language** | **Time** |
| ------------ | ---------|
| **Swift**    | 106.10s  |
| **C++**      | 129.38s  |
| **Rust**     | 138.07s  |

## Run benchmark

You can run the python script to quickly build and time the runs: ``python3 ./profile.py``

## Prerequisites

- Xcode CLT, quickly install with: ``xcode-select --install``

---

### C++

**Compiler version**: Apple clang version 16.0.0 (clang-1600.0.26.4)

- To build the project, run: ``xcodebuild -project ./_cpp/_cpp.xcodeproj``
- To profile the time, run: ``time ./_cpp/build/Release/_cpp``

The result on my end:
```
./_cpp/build/Release/_cpp  129.38s user 0.14s system 199% cpu 1:04.90 total
```

### Rust

**Compiler version**: rustc 1.82.0 (f6e511eec 2024-10-15)

- To build the project, run: ``cargo build --release --manifest-path ./_rust/Cargo.toml``
- To profile the time, run: ``time ./_rust/target/release/_rust``

The result on my end:
```
./_rust/target/release/_rust  138.07s user 0.13s system 198% cpu 1:09.66 total
```

### Swift

**Compiler version**: Apple Swift version 6.0.2 (swiftlang-6.0.2.1.2 clang-1600.0.26.4)

- To build the project, run: ``xcodebuild -project ./_swift/_swift.xcodeproj``
- To profile the time, run: ``time ./_swift/build/Release/_swift``

The result on my end:
```
./_swift/build/Release/_swift  106.10s user 0.11s system 198% cpu 53.448 total
```
