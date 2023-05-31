var xhr = new XMLHttpRequest();
xhr.open("GET", "https://api.openweathermap.org/data/2.5/weather?q=india&appid=YOUR_API_KEY");
xhr.onload = function() {
  if (xhr.status === 200) {
    var weatherData = JSON.parse(xhr.responseText);
    var temperature = weatherData.main.temp;
    var description = weatherData.weather[0].description;
    document.getElementById("weather").innerHTML = temperature + "°C, " + description;
  } else {
    alert("Error loading weather data");
  }
};
xhr.send();
