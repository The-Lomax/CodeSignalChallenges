let Blocks = [
    {
        "gym": false,
        "school": true,
        "store": false
    },
    {
        "gym": true,
        "school": false,
        "store": false
    },
    {
        "gym": true,
        "school": true,
        "store": false
    },
    {
        "gym": false,
        "school": true,
        "store": false
    },
    {
        "gym": false,
        "school": true,
        "store": true
    },
]
Reqs = ["gym", "school", "store"]

// find the location (block) with the lowest distance required to get to every building

const task = (buildings) => {
    let allFound = false;
    for (building of buildings) {
        while(!allFound) {
            for (req of Reqs) {
                
            }
        }

    }
}