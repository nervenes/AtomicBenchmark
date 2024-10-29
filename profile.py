#!/usr/bin/python3

import subprocess

subprocess.run(["xcodebuild", "-project", "./_cpp/_cpp.xcodeproj"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
result = subprocess.run(["time", "./_cpp/build/Release/_cpp"], capture_output=True, text=True)
print("C++", result.stderr.split()[2] + "s")

subprocess.run(["cargo", "build", "--release", "--manifest-path", "./_rust/Cargo.toml"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
result = subprocess.run(["time", "./_rust/target/release/_rust"], capture_output=True, text=True)
print("Rust", result.stderr.split()[2] + "s")

subprocess.run(["xcodebuild", "-project", "./_swift/_swift.xcodeproj"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
result = subprocess.run(["time", "./_swift/build/Release/_swift"], capture_output=True, text=True)
print("Swift", result.stderr.split()[2] + "s")
