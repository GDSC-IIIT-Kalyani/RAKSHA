var text = '{ "name":"John", "age":"39", "city":"New York"}';
var obj = JSON.parse(text, function (key, value) {
  if (key == "city") {
    return value.toUpperCase();
  } else {
    return value;
  }
});

document.getElementById("demo").innerHTML = obj.name + ", " + obj.city;