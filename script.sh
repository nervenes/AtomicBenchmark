#!/bin/zsh

set -e

xcodebuild -project ./_cpp/_cpp.xcodeproj > /dev/null
cargo build --release --quiet --manifest-path ./_rust/Cargo.toml > /dev/null
xcodebuild -project ./_swift/_swift.xcodeproj > /dev/null

time ./_cpp/build/Release/_cpp
time ./_rust/target/release/_rust
time ./_swift/build/Release/_swift
