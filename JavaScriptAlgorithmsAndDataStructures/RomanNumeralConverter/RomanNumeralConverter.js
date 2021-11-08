function convertToRoman(num) {
  let numStr = ("" + num).split("").reverse();
  let numRoman = "";

  for (let i = 0; i<numStr.length; i++) {
      if(i == 0){
          numRoman += convertUnityToRoman(parseInt(numStr[i]));
      }

      if(i == 1){
        numRoman += convertDozenToRoman(parseInt(numStr[i]));
    }

    if(i == 2){
        numRoman += convertHundredToRoman(parseInt(numStr[i]));
    }

    if(i == 3){
        numRoman += convertThousandToRoman(parseInt(numStr[i]));
    }
  }

  return numRoman.split("").reverse().join("");
}

function convertUnityToRoman(num){
    if(num < 4){
        return "I".repeat(num);
    }

    if(num < 5) {
        return "VI";
    }

    if(num<9){
        return "I".repeat(num-5)+"V";
    }

    return "XI";
}

function convertDozenToRoman(num){
    if(num < 4){
        return "X".repeat(num);
    }

    if(num < 5) {
        return "LX";
    }

    if(num<9){
        return "X".repeat(num-5)+"L";
    }

    return "CX";
}

function convertHundredToRoman(num){
    if(num < 4){
        return "C".repeat(num);
    }

    if(num < 5) {
        return "DC";
    }

    if(num<9){
        return "C".repeat(num-5)+"D";
    }

    return "MC";
}

function convertThousandToRoman(num){
    if(num < 5){
        return "M".repeat(num);
    }

    if(num<9){
        return "M".repeat(num-5)+"V";
    }

    return "XM";
}

var nums = {
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    9: "IX",
    12: "XII",
    16: "XVI",
    29: 'XXIX',
    44: 'XLIV',
    45: 'XLV',
    68: 'LXVIII',
    83: 'LXXXIII',
    97: 'XCVII',
    99: 'XCIX',
    400: 'CD',
    500: 'D',
    501: 'DI',
    649: 'DCXLIX',
    798: 'DCCXCVIII',
    891: 'DCCCXCI',
    1000: 'M',
    1004: 'MIV',
    1006: 'MVI',
    1023: 'MXXIII',
    2014: 'MMXIV',
    3999: 'MMMCMXCIX'
}

Object.entries(nums).forEach(i => {
    console.log(i[0] + " - " + i[1] + ": " +convertToRoman(i[0]) + " - equals? " + ((convertToRoman(i[0])===i[1])? "Yes" : "No"));
});
