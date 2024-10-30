# AtomicBenchmark

Benchmark of 20 billion atomic arithmetics in parallel.

### Benchmark results

These are the best results each language have had over numerous runs. Ranked from fastest to slowest:

| **Language**    | **User** | **System** | **CPU usage** | **Total** |
| --------------- | -------- | ---------- | ------------- | --------- |
| [Swift](#swift) | 64.70s   | 0.06s      | 199%          | 32.388    |
| [C++](#c++)     | 129.33s  | 0.21s      | 199%          | 1:04.96   |
| [Rust](#rust)   | 138.34s  | 0.12s      | 198%          | 1:09.81   |

> [!NOTE]
> These benchmarks was performed on the **Apple Silicon M3** chip in **macOS 15.1**.
>
> You can click on the language name to see which compiler and version was used, as well as instructions to build the project and time it.

### Running the benchmark

I've provided a script to quickly build each project and then time them.

- Make the script executable: ``chmod +x ./script.sh``
- Then run it: ``./script.sh``

> [!NOTE]
> Xcode CLT is required, install with: ``xcode-select --install``

## Compiler information and build instructions

### C++

**Compiler version**: Apple clang version 16.0.0 (clang-1600.0.26.4)

- Build the project: ``xcodebuild -project ./_cpp/_cpp.xcodeproj``
- Profile the time: ``time ./_cpp/build/Release/_cpp``

### Rust

**Compiler version**: rustc 1.82.0 (f6e511eec 2024-10-15)

- Build the project: ``cargo build --release --manifest-path ./_rust/Cargo.toml``
- Profile the time: ``time ./_rust/target/release/_rust``

### Swift

**Compiler version**: Apple Swift version 6.0.2 (swiftlang-6.0.2.1.2 clang-1600.0.26.4)

- Vuild the project: ``xcodebuild -project ./_swift/_swift.xcodeproj``
- Profile the time: ``time ./_swift/build/Release/_swift``
