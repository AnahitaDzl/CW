const age = Number(prompt("Please enter your age:"));

if (age >= 0 && age <= 10) {
  console.log("child");
} else if (age >= 11 && age <= 18) {
  console.log("teenager");
} else if (age >= 19 && age <= 30) {
  console.log("young person");
} else {
  console.log("adult");
}