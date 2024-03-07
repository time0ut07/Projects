/*
Own side project (Start 17/10/2022) (Can use but have minor bugs 22/10/2022) (Fixed bugs 27/10/2022)
*/

/*
Bugs:
NO BUGS


Ideas:
1. Allow me to put them into individual folders and select the folder first before selecting the topic
1.1. Create a whole new folder
1.2. Allow me to create folder in the root folder
1.3. Only allow me to delete the root folder if there isn't any folder inside
1.4. Allow me to delete folders in the root folder

2. Able to have a mode where I combine all the questions from all the lecture into 1 big quiz - If possible, able to pick which lecture to be included


=========================================================================================================================

3. Settings: Allow to see how many flashcard is left and have completed

4. When you answer the same questions correctly thrice, remove it from the main file and put it somewhere else
*/

const { question } = require("readline-sync");
const fs = require("fs");

//===================================================================
//                     Folder option 1 (Access)
//===================================================================

function accessfolders() {
  var directory = [],
    directories = fs.readdirSync(`${__dirname}`),
    choice;

  // Look at avaliable directories and push into an array [directory]

  for (i = 0; i < directories.length; i += 1) {
    if (i != 0) {
      directory.push(directories[i]);
    }
  }

  /*

  
  */

  var numofdir = directory.length;

  if (numofdir == 0) {
    console.log("\nYou do not have any folder... Go create some!");
    return;
  } else {
    console.log(
      '\nWhich folder would you like to access? (Type "CANCEL" to end process)'
    );

    // Displays all element from array [directory]
    for (i = 0; i < directory.length; i += 1) {
      console.log("\t" + (i + 1) + ". " + directory[i]);
    }

    // Ask for input to access directory, return input to main program

    do {
      choice = question(">> ");
      if (choice == "CANCEL") {
        return choice;
      } else if (choice < 1 || choice > numofdir || isNaN(choice) == true) {
        console.log("Please enter a valid input.\n");
      } else {
        return choice;
      }
    } while (choice < 1 || choice > numofdir || isNaN(choice) == true);
  }
}

//===================================================================
//                  Folders option 2 (Create)
//===================================================================

function createfolder() {
  var name;
  var directories = fs.readdirSync(`${__dirname}`);
  var directory = [];

  for (i = 0; i < directories.length; i += 1) {
    if (i != 0) {
      directory.push(directories[i]);
    }
  }

  // If name of new folder matches with existing folder, display ____

  do {
    match = false;
    name = question(
      '\nEnter folder\'s name\n(Type "CANCEL" to end process)\n >> '
    );

    if (name == "") {
      console.log("\nPlease enter a valid name.");
    } else {
      for (i = 0; i < fs.readdirSync(__dirname).length; i += 1) {
        if (name == fs.readdirSync(__dirname)[i]) {
          console.log("\nThis file already exists!");
          match = true;
        }
      }
      if (match == false) {
        fs.mkdirSync(name);
        console.log("\nFolder name, " + name + " , is created successfully.");

        var pathway = "" + __dirname + "\\" + name + "\\";
        fs.writeFileSync(pathway + name + "_Questions", "");
        fs.writeFileSync(pathway + name + "_Answers", "");
      }
    }
  } while (name == "" && name != "CANCEL");
}

//===================================================================
//                   Folder option 3 (Delete)
//===================================================================

function deletefolder() {
  var name;

  //Check if folder name exists and ask to confirm twice before deleting

  do {
    name = question(
      '\nEnter folder\'s name \n(Type "CANCEL" to end process)\n>> '
    );

    if (fs.existsSync(name) == false && name != "CANCEL") {
      console.log("\nPlease enter a valid folder name!");
    } else if (
      fs.existsSync(name) == true &&
      fs.readdirSync(name).length != 0
    ) {
      console.log(
        "\nThis folder have files in it. Delete them first before deleting the folder."
      );
    } else if (fs.existsSync(name) == true) {
      do {
        confirming = question("\nDelete " + name + "?\n1. Yes    2. No\n>> ");

        if (confirming != 1 && confirming != 2) {
          console.log("\nPlease enter a valid input!");
        }
      } while (confirming != 1 && confirming != 2);

      if (confirming == 1) {
        do {
          confirm2 = question(
            "\nAre you sure you want to delete this folder (" +
              name +
              ") ? \n1. Yes   2. No\n>> "
          );

          if (confirm2 == 1) {
            fs.rmdirSync(name);
            console.log("\nFolder " + name + " deleted");
            return;
          } else if (confirm2 == 2) {
            console.log("\nProcess stopped.");
          } else {
            console.log("\nPlease enter a valid input!");
          }
        } while (confirm2 != 2 && confirm2 != 1);
      } else if (confirming == 2) {
        console.log("\nProcess stopped.");
      }
    } else if (name == "CANCEL") {
      console.log("\nYou have cancelled this process.\n");
    }
  } while (
    name != "CANCEL" &&
    fs.existsSync(name) == false &&
    fs.existsSync(name) == true &&
    fs.readdirSync(directoryname).length != 0
  );
}

//===================================================================
//                  Folder option 4 (Delete files)
//===================================================================

function deletefiles() {
  var directory = [],
    directories = fs.readdirSync(`${__dirname}`),
    choice;

  // Look at avaliable directories and push into an array [directory]

  for (i = 0; i < directories.length; i += 1) {
    if (i != 0) {
      directory.push(directories[i]);
    }
  }

  console.log(
    '\nWhich folder would you like to access to delete the files? (Type "CANCEL" to end process)'
  );

  // Displays all element from array [directory]

  for (i = 0; i < directory.length; i += 1) {
    console.log("\t" + (i + 1) + ". " + directory[i]);
  }

  var numofdir = directory.length;

  // Ask for input to access directory, return input to main program

  do {
    choice = question(">> ");

    if (choice == "CANCEL") {
      return choice;
    } else if (choice < 1 || choice > numofdir || isNaN(choice) == true) {
      console.log("Please enter a valid input.\n");
    } else {
      return choice;
    }
  } while (choice < 1 || choice > numofdir || isNaN(choice) == true);
}

//===================================================================
//                     Flashcard option 1 (Play)
//===================================================================

function UseFlashcards() {
  //Pushes contents in file line by line to form an array

  var pathway = "" + __dirname + "\\" + directoryname + "\\";

  var QuestionArray = fs
    .readFileSync(pathway + directoryname + "_Questions")
    .toString()
    .split("\n");
  var AnswerArray = fs
    .readFileSync(pathway + directoryname + "_Answers")
    .toString()
    .split("\n");

  NumOfQuestions = QuestionArray.length;

  //If folder empty ______

  if (NumOfQuestions == 0) {
    console.log("\nThere is no flashcard... Go create some!");
  }

  var TempQuestion = [];
  var TempAnswer = [];
  //var correct = 0

  //Randomly generates a number to push and display the element to a temp array until temp array == original array

  for (i = 0; i < NumOfQuestions - 1; i += 1) {
    var random = 1 + Math.floor(Math.random() * (QuestionArray.length - 1));

    if (QuestionArray.length == 1) {
      random = 1;
    }

    TempQuestion.push(QuestionArray[random]);
    TempAnswer.push(AnswerArray[random]);

    QuestionArray.splice(random, 1);
    AnswerArray.splice(random, 1);

    do {
      console.log(
        "===================================================================================================="
      );

      InputAnswer = question(
        "\n" + TempQuestion[i] + '\n(Type "CANCEL" to end process)\n>> '
      );

      if (InputAnswer == "") {
        console.log("\nPlease enter a valid Answer!");
      } else if (InputAnswer == "CANCEL") {
        console.log("\nStopping process...");
        return;
      } else if (InputAnswer.toLowerCase() == TempAnswer[i].toLowerCase()) {
        console.log("\nCorrect!");
        //correct += 1
      } else {
        console.log("\nProper Answer is...");
        console.log("< " + TempAnswer[i] + " >");
      }
    } while (InputAnswer == "" && InputAnswer != "CANCEL");
  }

  //console.log("Your score: " + correct + "/" + (NumOfQuestions-1))

  TempAnswer = [];
  TempQuestion = [];
}

//===================================================================
//                 Flashcards option 2 (Create)
//===================================================================

function AddFlashcard() {
  var pathway = "" + __dirname + "\\" + directoryname + "\\";

  //In case user delete files by accident

  if (fs.readdirSync(directoryname).length == 0) {
    fs.writeFileSync(pathway + directoryname + "_Questions", "");
    fs.writeFileSync(pathway + directoryname + "_Answers", "");
  }

  var exit = false;

  //Asked to type in a question and an answer before appending the file

  while (exit == false) {
    do {
      var AddQuestion = question(
        '\nType in your QUESTION\n(Type "CANCEL" to end process)\n>> '
      );
      if (AddQuestion == "CANCEL") {
        console.log("\nStopping process...");
        exit = true;
      } else if (AddQuestion == "") {
        console.log("\nPlease enter a valid input.");
      } else {
        do {
          var AddAnswer = question(
            '\nType in the ANSWER\n(Type "CANCEL" to end process)\n>> '
          );

          if (AddAnswer == "CANCEL") {
            console.log("\nStopping process...");
            exit = true;
          } else if (AddAnswer == "") {
            console.log("\nPlease enter a valid input.");
          } else {
            fs.appendFileSync(pathway + directoryname + "_Answers", "\n");
            fs.appendFileSync(pathway + directoryname + "_Questions", "\n");

            fs.appendFileSync(pathway + directoryname + "_Answers", AddAnswer);
            fs.appendFileSync(
              pathway + directoryname + "_Questions",
              AddQuestion
            );
            console.log("\nSuccessfully added new flashcard!");
            return;
          }
        } while (AddAnswer != "CANCEL");
      }
    } while (
      AddQuestion != "CANCEL" &&
      AddAnswer != "CANCEL" &&
      AddQuestion != "" &&
      AddAnswer != ""
    );
  }
}

//===================================================================
//            Flashcards option 3 (Edit/Delete)
//===================================================================

function DeleteOrEditFlashcard() {
  var next = 1;

  //Content in file line by line to form an array

  question("\nPress [Enter] to start editing!\n>> ");

  var pathway = "" + __dirname + "\\" + directoryname + "\\";

  var QuestionArray = fs
    .readFileSync(pathway + directoryname + "_Questions")
    .toString()
    .split("\n");
  var AnswerArray = fs
    .readFileSync(pathway + directoryname + "_Answers")
    .toString()
    .split("\n");

  if (QuestionArray.length == 1) {
    console.log("\nFile is empty! Go create flashcards.");
    return;
  }

  //Sub menu to move around

  do {
    console.log(
      "===================================================================================================="
    );
    console.log("\n\n\nQuestion: " + QuestionArray[next]);
    console.log("Answer: " + AnswerArray[next]);
    console.log("\n\t\t\t[" + next + "/" + (QuestionArray.length - 1) + "]");

    var DelOrEdit = question(
      "\n1. Next    2. Previous   3. Edit      4. Delete     5. Exit\n>> "
    );

    if (DelOrEdit == "") {
      console.log("\nPlease enter a valid input!");
    } else if (DelOrEdit == 1) {
      next += 1;

      if (next == QuestionArray.length) {
        console.log("\nNo more flashcards");
      }
    } else if (DelOrEdit == 2) {
      if (next == 1) {
        console.log("\nThis is the first flashcard!");
      } else {
        next -= 1;
      }
    } else if (DelOrEdit == 3) {
      do {
        console.log(
          "===================================================================================================="
        );
        console.log("\n\n\n\nQuestion: " + QuestionArray[next]);
        console.log("Answer: " + AnswerArray[next]);

        //Sub menu

        var editing = question(
          "\n1. Edit question   2. Edit Answer    3. Back\n>> "
        );

        if (editing != 1 && editing != 2 && editing != 3) {
          console.log("\nPlease enter a valid input!\n");
        } else if (editing == 1) {
          //If editing, need to confirm twice before changing

          console.log("\n" + QuestionArray[next]);
          console.log(AnswerArray[next]);

          do {
            changefc = question("\nEnter new QUESTION: ");

            if (changefc == "") {
              console.log("\nPlease enter a valid input!");
            } else {
              do {
                var exit = false;

                confirm1 = question(
                  "\nAre you sure you want to edit this question from \n\n" +
                    QuestionArray[next] +
                    "   to\n" +
                    changefc +
                    "\n\n1. Yes   2. No\n>> "
                );

                if (confirm1 != 1 && confirm1 != 2) {
                  console.log("\nPlease enter a valid input!");
                } else if (confirm1 == 1) {
                  console.log("\nSuccessfully changed question!");

                  //Changes the element in the array to new question

                  for (i = 0; i < QuestionArray.length; i += 1) {
                    if (QuestionArray[i] == QuestionArray[next]) {
                      const index = QuestionArray.indexOf(QuestionArray[i]);

                      if (index !== -1) {
                        QuestionArray[index] = changefc;
                      }
                    }
                  }

                  //Clear all file content

                  fs.writeFile(
                    pathway + directoryname + "_Questions",
                    "",
                    function () {}
                  );

                  //Appending the file line by line using the array

                  for (i = 1; i != QuestionArray.length; i += 1) {
                    fs.appendFileSync(
                      pathway + directoryname + "_Questions",
                      "\n"
                    );

                    var Array2String = QuestionArray[i].toString();

                    fs.appendFileSync(
                      pathway + directoryname + "_Questions",
                      Array2String
                    );
                  }

                  exit == true;
                } else if (confirm1 == 2) {
                  console.log("Not editing question...");
                  exit == true;
                }
              } while (exit != false);
            }
          } while (changefc != "" && exit != false);
        } else if (editing == 2) {
          console.log("\n" + QuestionArray[next]);
          console.log(AnswerArray[next]);

          do {
            changefc = question("\nEnter new ANSWER: ");

            if (changefc == "") {
              console.log("\nPlease enter a valid input!");
            } else {
              do {
                var exit = false;

                confirm1 = question(
                  "\nAre you sure you want to edit this answer from \n\n" +
                    AnswerArray[next] +
                    "   to\n" +
                    changefc +
                    "\n\n1. Yes   2. No\n>> "
                );

                if (confirm1 != 1 && confirm1 != 2) {
                  console.log("\nPlease enter a valid input!");
                } else if (confirm1 == 1) {
                  console.log("\nSuccessfully changed question!");

                  for (i = 0; i < AnswerArray.length; i += 1) {
                    if (AnswerArray[i] == AnswerArray[next]) {
                      const index = AnswerArray.indexOf(AnswerArray[i]);

                      if (index !== -1) {
                        AnswerArray[index] = changefc;
                      }
                    }
                  }

                  fs.writeFile(
                    pathway + directoryname + "_Answers",
                    "",
                    function () {}
                  );

                  for (i = 1; i != AnswerArray.length; i += 1) {
                    fs.appendFileSync(
                      pathway + directoryname + "_Answers",
                      "\n"
                    );

                    var Array2String = AnswerArray[i].toString();

                    fs.appendFileSync(
                      pathway + directoryname + "_Answers",
                      Array2String
                    );
                  }

                  exit == true;
                } else if (confirm1 == 2) {
                  console.log("Not editing question...");
                  exit == true;
                }
              } while (exit != false);
            }
          } while (changefc != "" && exit != false);
        }
      } while (editing != 3);
    } else if (DelOrEdit == 4) {
      var exit = false;

      //Asked to confirm twice before deleting

      do {
        var confirm1 = question(
          "\nAre you sure you want to delete this flashcard permanently? (1. Continue 2.  Cancel)\nQuestions: " +
            QuestionArray[next] +
            "\nAnswer: " +
            AnswerArray[next] +
            "\n>> "
        );

        if (confirm1 != 1 && confirm1 != 2) {
          console.log("\nPlease enter a valid input!");
        } else if (confirm1 == 1) {
          do {
            var confirm2 = question(
              "\nThis flashcard will be gone forever. (1. Continue 2. Cancel)\n>> "
            );

            if (confirm2 != 1 && confirm2 != 2) {
              console.log("\nPlease enter a valid input!");
            } else if (confirm2 == 1) {
              QuestionArray.splice(next, 1);
              AnswerArray.splice(next, 1);

              //Clear all file content from both file

              fs.writeFile(
                pathway + directoryname + "_Questions",
                "",
                function () {}
              );
              fs.writeFile(
                pathway + directoryname + "_Answers",
                "",
                function () {}
              );

              //Appending the file with the changed array

              for (v = 1; v != AnswerArray.length; v += 1) {
                fs.appendFileSync(pathway + directoryname + "_Questions", "\n");

                var Array2String = QuestionArray[v].toString();

                fs.appendFileSync(
                  pathway + directoryname + "_QUestions",
                  Array2String
                );
              }

              for (p = 1; p != AnswerArray.length; p += 1) {
                fs.appendFileSync(pathway + directoryname + "_Answers", "\n");

                var Array2String = AnswerArray[p].toString();

                fs.appendFileSync(
                  pathway + directoryname + "_Answers",
                  Array2String
                );
              }

              exit = true;
            } else if (confirm2 == 2) {
              console.log("\nStopping process...");
              exit = true;
            }
          } while (
            (confirm2 != 1 || confirm2 != 2) &&
            exit == false &&
            CONFIRM2 != 2
          );
        } else if (confirm1 == 2) {
          console.log("\nStopping process...");
        }
      } while (
        confirm1 != 2 &&
        confirm2 != 2 &&
        (confirm1 != 1 || confirm1 != 2) &&
        exit == false
      );
    } else if (DelOrEdit == 5) {
      console.log("Exiting process...");
    }
  } while (DelOrEdit != 5 && next != QuestionArray.length);
}

//===================================================================
//            Flashcards option 4 (Delete Folder)
//===================================================================

function deleteFolder() {

}

//===================================================================
//                        Main Program
//===================================================================

do {
  var foldchoice = question(
    "\nWelcome to time0ut Flash Card, what would you like to do?\n(Everything is case sensitive)\n\t1. Access Folders\n\t2. Create Folder\n\t3. Delete Folder\n\t4. Delete files\n\t5. Exit\n>> "
  );

  if (
    foldchoice < 1 ||
    foldchoice > 5 ||
    isNaN(foldchoice) == true ||
    foldchoice % 1 != 0
  ) {
    console.log("Please enter a valid input.");
  } else if (foldchoice == 1) {
    var folderchoice = accessfolders();

    if (folderchoice != "CANCEL") {
      //form an array from all directories

      var directory = [],
        directories = fs.readdirSync(`${__dirname}`);

      for (i = 0; i < directories.length; i += 1) {
        if (i != 0) {
          directory.push(directories[i]);
        }
      }

      var directoryname = directory[folderchoice - 1];

      do {
        var whattodo = question(
          "\nWhat would you like to do in the folder " +
            directoryname +
            "?\n\t1. Use Flashcards\n\t2. Add Flashcard\n\t3. Delete or Edit flashcard\n\t4. Exit Folder\n>> "
        );

        if (whattodo == 1) {
          UseFlashcards();
        } else if (whattodo == 2) {
          AddFlashcard();
        } else if (whattodo == 3) {
          DeleteOrEditFlashcard();
        } else if (whattodo == 4) {
          console.log("\nExiting folder...");
        } else {
          console.log("\nPlease enter a valid input.");
        }
      } while (whattodo != 4);
    } else {
      console.log("\nExiting Folder...");
    }
  } else if (foldchoice == 2) {
    createfolder();
  } else if (foldchoice == 3) {
    deletefolder();
  } else if (foldchoice == 4) {
    //Mini code to delete file (Too lz to put in a function)

    var folderchoice1 = deletefiles();

    do {
      if (folderchoice1 != "CANCEL") {
        //form an array from all directories
        var directory = [],
          directories = fs.readdirSync(`${__dirname}`);

        for (i = 0; i < directories.length; i += 1) {
          if (i != 0) {
            directory.push(directories[i]);
          }
        }

        var directoryname = directory[folderchoice1 - 1];

        do {
          var whattodo1 = question(
            "\nYou WILL delete both Question and Answer file together in " +
              directoryname +
              "... Are you sure you want to do that?\n1. Yes    2. No\n>> "
          );

          if (whattodo1 != 1 && whattodo1 != 2) {
            console.log("\nPlease enter a valid input!");
          } else if (whattodo1 == 1) {
            do {
              var pathway = "" + __dirname + "\\" + directoryname + "\\";

              confirm1 = question(
                "\nAre you really sure you want to delete this file in " +
                  directoryname +
                  "... All content will be permanently deleted.\nPress [CONFIRM] or [CANCEL]\n>> "
              );

              if (confirm1 != "CANCEL" && confirm1 != "CONFIRM") {
                console.log("\nPlease enter a valid input!");
              } else if (confirm1 == "CONFIRM") {
                fs.unlinkSync(pathway + directoryname + "_Answers");
                fs.unlinkSync(pathway + directoryname + "_Questions");

                console.log("\nFile successfully deleted!");
              }
            } while (confirm1 != "CANCEL" && confirm1 != "CONFIRM");
          } else {
            console.log("\nExiting process...");
          }
        } while (
          whattodo1 != 2 &&
          confirm1 != "CANCEL" &&
          confirm1 != "CONFIRM"
        );
      } else {
        console.log("\nExiting Folder...");
      }
    } while (
      folderchoice1 != "CANCEL" &&
      whattodo1 != 2 &&
      confirm1 != "CANCEL" &&
      confirm1 != "CONFIRM"
    );
  } else if (foldchoice == 5) {
    console.log("\nThank you for choosing time0ut flashcards!");
  }
} while (foldchoice != 5);
