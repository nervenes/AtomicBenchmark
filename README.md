# AtomicBenchmark

Benchmark of 20 billion atomic arithmetics in parallel.

- **CPU**: Apple Silicon M3
- **OS**: macOS 15.1

## Benchmark Results

| **Language** | **User time** | **System time** | **CPU utilization** |
| ------------ | ------------- | --------------- | ------------------- |
| **Swift**    | 108,59s       | 0,09s           | 189%                |
| **Rust**     | 132,27s       | 0,09s           | 194%                |
| **C++**      | 146,15s       | 0,14s           | 199%                |

---

### C++

**Compiler version**: Apple clang version 16.0.0 (clang-1600.0.26.4)

- To build the project, run: ``xcodebuild -project ./_cpp/_cpp.xcodeproj``
- To profile the time, run: ``time ./_cpp/build/Release/_cpp``

The result on my end:
```
./_cpp/build/Release/_cpp  146,15s user 0,14s system 199% cpu 1:13,40 total
```

### Rust

**Compiler version**: rustc 1.82.0 (f6e511eec 2024-10-15)

- To build the project, run: ``cargo build --release --manifest-path ./_rust/Cargo.toml``
- To profile the time, run: ``time ./_rust/target/release/_rust``

The result on my end:
```
./_rust/target/release/_rust  132,27s user 0,09s system 194% cpu 1:07,90 total
```

### Swift

**Compiler version**: Apple Swift version 6.0.2 (swiftlang-6.0.2.1.2 clang-1600.0.26.4)

- To build the project, run: ``xcodebuild -project ./_swift/_swift.xcodeproj``
- To profile the time, run: ``time ./_swift/build/Release/_swift``

The result on my end:
```
./_swift/build/Release/_swift  108,59s user 0,09s system 189% cpu 57,344 total
```
