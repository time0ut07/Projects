// Start and finish 28/10/2022

const { question } = require("readline-sync");
const fs = require('fs');
var pathway = '' +  __dirname + "\\"
var BlockArray = fs.readFileSync((pathway + "block1")).toString().split("\n")

//const hash = crypto.createHash('sha256').digest('base64');
const {createHash} = require('crypto');

// lines: array of strings
function hash(lines) {
  const hash = createHash('sha256');
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim(); // remove leading/trailing whitespace
    if (line === '') continue; // skip empty lines
    hash.write(line); // write a single line to the buffer
  }

  return hash.digest('Hex'); // returns hash as string can use Base64
}

content = ''

for (i = 0; i < BlockArray.length; i += 1) {
  content += BlockArray[i]
}

//fs.writeFile((pathway + "block1hash"), '',function(){})
fs.appendFileSync((pathway + "block1hash"), (hash(content)) + "\n")


console.log("Hashed") 
