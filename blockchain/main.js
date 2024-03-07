// Start and finish 28/10/2022

const { question } = require("readline-sync");
const fs = require('fs');

var repeat = 0

do {

    var sender = question("\nSender: ")
    var receiver = question("Receiver: ")
    var amount = question("Amount: $")
    var transaction = sender + " sent " + receiver + " $" + amount
    var pathway = '' +  __dirname + "\\"
    repeat += 1
 
    console.log("\nTransaction successfully added!")
    fs.appendFileSync((pathway + "block1"), (transaction) + "\n")
    

    

} while (repeat != 3)
