function telephoneCheck(str) {
    const re = /^[1]?[ ]?(([(][0-9]{3}[)])|([0-9]{3}))[- ]?[0-9]{3}[- ]?[0-9]{4}$/;
    return re.test(str);
}

const testCases = {
    "555-555-5555" : true,
    "5555555555" : true,
    "1 555-555-5555" : true,
    "1 (555) 555-5555": true,
    "(555)555-5555" : true,
    "1(555)555-5555": true,
    "555-5555": false,
    "5555555": false,
    "1 555)555-5555": false,
    "1 555 555 5555": true,
    "1 456 789 4444": true,
    "123**&!!asdf#": false,
    "55555555": false,
    "(6054756961)": false,
    "2 (757) 622-7382": false,
    "0 (757) 622-7382": false,
    "-1 (757) 622-7382": false,
    "2 757 622-7382": false,
    "10 (757) 622-7382": false,
    "27576227382": false,
    "(275)76227382": false,
    "2(757)6227382": false,
    "2(757)622-7382": false,
    "555)-555-5555": false,
    "(555-555-5555": false,
    "(555)5(55?)-5555": false,
    "55 55-55-555-5": false
}

Object.entries(testCases).forEach((i) => {
    console.log(
      i[0] +
        " -> " +
        i[1] +
        " - Answer: " +
        telephoneCheck(i[0]) +
        " - equals? " +
        (telephoneCheck(i[0]) === i[1] ? "Yes" : "No")
    );
  });
