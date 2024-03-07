// Start and finish 28/10/2022

// Changes the content in block. Then just run hash and mine to see diff

const { question } = require("readline-sync");
const fs = require('fs');

var pathway = '' +  __dirname + "\\"
var next = 0
var HashArray = fs.readFileSync((pathway + "block1")).toString().split("\n")

console.log("\nChange transaction...\n")


do {
    choice = question("\n" + HashArray[next] + " \n\n1. Edit Transaction    2. Next Transaction    3. Previous Transaction    4. Exit\n>>")

    if (choice < 1 || choice > 4 || isNaN(choice) == true || choice % 1 != 0) {
        console.log("\nPlease enter a valid input")
    }

    else if (choice == 1) {
        changetrans = question("\nEdit transaction to: ")


        //Changes the element in the array to new question

        for (i = 0; i < HashArray.length; i += 1) {
            if (HashArray[i] == HashArray[next]) {

                const index = HashArray.indexOf(HashArray[i])

                if (index !== -1) {
                    HashArray[index] = changetrans
                }
            }
        }

        //Clear all file content

        fs.writeFile((pathway + "block1"), '',function(){})

        //Appending the file line by line using the array

        for (i = 0; i < HashArray.length; i += 1) {

            var Array2String = HashArray[i].toString()

            fs.appendFileSync((pathway + "block1"), (Array2String) + "\n",);
        }

    }

    else if (choice == 2) {
        next += 1

        if (next == (HashArray.length)) {
            console.log("\nEnd of block")
        }
    }

    else if (choice == 3) {
        if (next == 0) {
            console.log("\nThis is the first transaction!")
        }    
        else {
            next -= 1
        }
    }

} while (choice != 4 && next != HashArray.length-1)
