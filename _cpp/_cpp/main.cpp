//
//  main.cpp
//  _cpp
//
//  Created by Evren Sen on 2024-10-29.
//

#include <iostream>
#include <memory>
#include <atomic>
#include <thread>

std::atomic<size_t> counter;

void add() {
    std::size_t iterations = 10000000000;

    while (iterations != 0) {
        counter.fetch_add(1, std::memory_order_relaxed);
        iterations -= 1;
    }
}

void sub() {
    std::size_t iterations = 10000000000;

    while (iterations != 0) {
        counter.fetch_sub(1, std::memory_order_relaxed);
        iterations -= 1;
    }
}

int main() {
    counter.store(0, std::memory_order_relaxed);

    std::thread add_thread(add);
    std::thread sub_thread(sub);

    add_thread.join();
    sub_thread.join();
}
