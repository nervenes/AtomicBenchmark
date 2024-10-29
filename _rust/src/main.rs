//
//  main.rs
//  _rust
//
//  Created by Evren Sen on 2024-10-29.
//

use std::{
    sync::atomic::{AtomicIsize, Ordering},
    thread,
};

fn main() {
    static COUNTER: AtomicIsize = AtomicIsize::new(0);

    let add_handle = thread::spawn(move || {
        let mut iterations = 10000000000i64;

        while iterations != 0 {
            COUNTER.fetch_add(1, Ordering::Relaxed);
            iterations -= 1;
        }
    });

    let sub_handle = thread::spawn(move || {
        let mut iterations = 10000000000i64;

        while iterations != 0 {
            COUNTER.fetch_sub(1, Ordering::Relaxed);
            iterations -= 1;
        }
    });

    add_handle.join().unwrap();
    sub_handle.join().unwrap();
}
