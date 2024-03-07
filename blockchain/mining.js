// Start and finish 28/10/2022

/*
1. Take the hash value of the block
2. Find nounces ((hash value)+nounce) = validated block eg. N 0s in front
3. Update the validated hash
*/

const { question } = require("readline-sync");
const fs = require('fs');
var pathway = '' +  __dirname + "\\"
var HashArray = fs.readFileSync((pathway + "block1hash")).toString().split("\n")

//const hash = crypto.createHash('sha256').digest('base64');
const {createHash, Hash} = require('crypto');

// lines: array of strings
function hash(lines) {
  const hash = createHash('sha256');
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim(); // remove leading/trailing whitespace
    if (line === '') continue; // skip empty lines
    hash.write(line); // write a single line to the buffer
  }

  return hash.digest('Hex'); // returns hash as string can be Base64
}

var nonce = 0

if (HashArray.length == 1) {
  var use = HashArray[0]
} else {
  var use = HashArray[1]
}
var FinalBlockHash = hash(use + nonce)

var indivchar = (Array.from(FinalBlockHash)) // Splits each character to an indiv element
//console.log(indivchar)

while (indivchar[0] != '0' || indivchar[1] != '0' || indivchar[2] != '0' || indivchar[3] != '0' || indivchar[4] != '0') {
    nonce += 1

    var FinalBlockHash = hash(use + nonce)

    var indivchar = (Array.from(FinalBlockHash))
}

indivchar = Array.from(FinalBlockHash);

fs.appendFileSync((pathway + "finalblock1hash"), (FinalBlockHash) + "\n")

console.log(indivchar)
console.log("Nonce: " + nonce)
