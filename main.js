var map = L.map('map').setView([52.505, 13.41], 11);

L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 18,
}).addTo(map);


L.geoJson([geojson], {
  style: function (feature) {
    if (feature.properties.gender === "unknown"){
      return {color: "grey"};
    }
    else if (feature.properties.gender === "male"){
      return {color: "blue"};
    }
  },
}).addTo(map);
