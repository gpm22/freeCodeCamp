function rot13(str) {
  let arrayStr = Array.from(str);
  let newStr = "";
  let charChange;

  for (let i = 0; i < arrayStr.length; i++) {
    if (arrayStr[i].charCodeAt(0) > 64 && arrayStr[i].charCodeAt(0) < 91) {
      if (arrayStr[i].charCodeAt(0) < 78) {
        charChange = String.fromCharCode(arrayStr[i].charCodeAt(0) + 13);
      } else {
        charChange = String.fromCharCode(arrayStr[i].charCodeAt(0) - 13);
      }
    } else {
      charChange = arrayStr[i];
    }

    newStr += charChange;
  }

  return newStr;
}

const testCases = {
  "SERR PBQR PNZC": "FREE CODE CAMP",
  "SERR CVMMN!": "FREE PIZZA!",
  "SERR YBIR?": "FREE LOVE?",
  "GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT.":
    "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.",
};

Object.entries(testCases).forEach((i) => {
  console.log(
    i[0] +
      " -> " +
      i[1] +
      " - Answer: " +
      rot13(i[0]) +
      " - equals? " +
      (rot13(i[0]) === i[1] ? "Yes" : "No")
  );
});
