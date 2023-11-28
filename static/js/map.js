let config = {
  minZoom: 7,
  maxZoom: 18,
	attributionControl: false,
};

// magnification with which the map will start
const zoom = 16;
// co-ordinates
const lat = 52.2613;
const lng = 104.2655;

const map = L.map('map', config).setView([lat, lng], zoom);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
		attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);