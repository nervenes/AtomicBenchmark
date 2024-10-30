# AtomicBenchmark

Benchmark of 20 billion atomic arithmetics in parallel.

### Benchmark results

These are the best results each language have had over numerous runs. Ranked from fastest to slowest:

| **Language**    | **User** | **System** | **CPU usage** | **Total** |
| --------------- | -------- | ---------- | ------------- | --------- |
| [Swift](#swift) | 66,55s   | 0,04s      | 158%          | 41,921    |
| [Rust](#rust)   | 117,80s  | 0,08s      | 183%          | 1:04,31   |
| [C++](#cpp)     | 119,43s  | 0,09s      | 195%          | 1:00,99   |

> [!NOTE]
> These benchmarks was performed on a **Apple Silicon M3** chip in **macOS 15.1**.
>
> You can click on the language name to see which compiler and version was used, as well as instructions to build the project and time it.

### Running the benchmark

There is a zsh script in the root of the repo that builds each project and then times them.

- Make the script executable: ``chmod +x ./script.sh``
- Then run a single benchmark with: ``./script.sh``. You can also pass a number like so ``./script.sh 3`` to run the benchmark 3 times.

> [!NOTE]
> Xcode CLT is required, install with: ``xcode-select --install``

## Compiler information and build instructions

### Cpp

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
