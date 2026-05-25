var choice = prompt("Welcome to Area Calculator. \n Please Enter your Choice. \n1.Area of Rectangle. \n2.Area of Triangle. \n3.Area of Circle.");

if (choice == '1') {
  var length = prompt('Enter the Length')
  var width = prompt('Enter the width')
  var result =length*width
  alert('The Area is '+ result)
}
if (choice == '2') {
  var height = prompt('Enter the height')
  var base = prompt('Enter the base')
  var area = height*(base) /2
  alert('The Area is '+ area)
}
if (choice == '3') {
  var radius = prompt('Enter the radius')
  var result = 3.14*radius*radius
  alert('The Area is '+ result)
}