const numbers = [2, 1, 3, 4, 6, 8, 7, 9, 5];
const newNumbers = [];

numbers.sort(function (a, b) {
  return a - b;
});
let highest = numbers[numbers.length - 1];
console.log(numbers);

numbers.sort(function (a, b) {
  return b - a;
});

let lowest = numbers[0];
console.log(numbers);
