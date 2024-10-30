//
//  main.swift
//  _swift
//
//  Created by Evren Sen on 2024-10-29.
//

import Synchronization

let counter = Atomic<Int32>(0)

await withTaskGroup(of: Void.self) { group in
    group.addTask {
        var iterations: Int64 = 10000000000

        while iterations != 0 {
            counter.add(1, ordering: .relaxed)
            iterations -= 1
        }
    }

    group.addTask {
        var iterations: Int64 = 10000000000

        while iterations != 0 {
            counter.subtract(1, ordering: .relaxed)
            iterations -= 1
        }
    }
}
