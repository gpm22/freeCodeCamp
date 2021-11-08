function palindrome(str) {

  let cleanStr = str.slice().replace(/[^A-Za-z0-9]/g, '').toUpperCase();

  let half;
  let firstHalf;
  let secondHalf;

  if(cleanStr.length % 2 === 0){
    half = cleanStr.length/2;
    firstHalf = cleanStr.slice(0, half);
    secondHalf = cleanStr.slice(half);
  } else {
    half = Math.floor(cleanStr.length/2);
    firstHalf = cleanStr.slice(0, half);
    secondHalf = cleanStr.slice(half+1);
  }
  
  secondHalf=secondHalf.split("").reverse().join("");

  //console.log("word: " + str + " - clean word: " +cleanStr +" - firstHalf: " + firstHalf + " - secondHalf: " + secondHalf);
  return firstHalf === secondHalf;
}

console.log("eye - true: " + palindrome("eye"));
console.log("_eye - true: " + palindrome("_eye"));
console.log("race car - true: " + palindrome("race car"));
console.log("not a palindrome - false: "+ palindrome("not a palindrome"));
console.log("A man, a plan, a canal. Panama - true: " + palindrome("A man, a plan, a canal. Panama"));
console.log("never odd or even - true: "+palindrome("never odd or even"));
console.log("nope - false: "+palindrome("nope"));
console.log("almostomla - false: "+palindrome("almostomla"));
console.log("My age is 0, 0 si ega ym. - true: "+palindrome("My age is 0, 0 si ega ym."));
console.log("1 eye for of 1 eye. - false: "+palindrome("1 eye for of 1 eye."));
console.log("0_0 (: /-\ :) 0-0 - true: "+palindrome("0_0 (: /-\ :) 0-0"));
console.log("five|\_/|four - false: "+palindrome("five|\_/|four"));
