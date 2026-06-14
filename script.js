async function getWeather() {

    const city = document.getElementById("city").value;
    const result = document.getElementById("result");

    if(city === ""){
        result.innerHTML = "Please enter a city.";
        return;
    }

    try{
        const response = await fetch(`/weather?city=${city}`);
        const data = await response.json();

        if(data.error){
            result.innerHTML = data.error;
            return;
        }

        result.innerHTML = `
            <h3>${data.city}</h3>
            <p>Temperature: ${data.temp} °C</p>
            <p>Humidity: ${data.humidity}%</p>
            <p>Weather: ${data.weather}</p>
        `;

    }catch(error){
        result.innerHTML = "Error fetching weather data.";
    }
}