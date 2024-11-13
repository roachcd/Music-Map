<template>
  <div class="home">
    <div id="map"></div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import "leaflet/dist/leaflet.css";
import L from "leaflet";


var weightData = require("@/assets/WeightData/United States of America.json");
var weightDataJson = JSON.parse(JSON.stringify(weightData));

function getWeightData(country){
  try{
    weightData = require("@/assets/WeightData/"+country+".json");
    weightDataJson = JSON.parse(JSON.stringify(weightData));
  }
  catch{
    console.log("No data for " + country);
  }
}

var countryMap = null;
var info = L.control();

info.onAdd = function (map) {
    this.update();
};

info.update = function (props) {
  console.log(props.name);
  getWeightData(props.name);
  countryMap.resetStyle();
}

function highlightFeature(e) {
    var layer = e.target;
    info.update(layer.feature.properties);

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });

    layer.bringToFront();
}

function resetHighlight(e) {
    countryMap.resetStyle(e.target);
} 

function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}

function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature
    });
}

function getColor(country) {

    console.log(country);

    const result = weightDataJson.filter(item => item.name === country);

    //console.log(result);

    if(result.length != 0){
      const d = result[0].weight;
      console.log(d);

      return d > 70 ? '#800026' :
            d > 60  ? '#BD0026' :
            d > 50  ? '#E31A1C' :
            d > 40  ? '#FC4E2A' :
            d > 30   ? '#FD8D3C' :
            d > 20   ? '#FEB24C' :
            d > 10   ? '#FED976' :
                        '#FFEDA0';
    }
    else{
      return '#FFEDA0';
    }

}

function style(feature) {
    return {
        fillColor: getColor(feature.properties.name),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}


export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  methods:{
    setupLeafletMap: function () {
      const map = L.map('map').setView([51.505, -0.09], 13);

      const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 5,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(map);

      var countryData = require("@/assets/globe.geo.json")
      countryMap = new L.geoJson(countryData, {style: style, onEachFeature: onEachFeature});
      countryMap.addTo(map);

      info.addTo(map);
      
    },
  },
  mounted() {
   this.setupLeafletMap();
 },
}
</script>

<style>
#map { height: 1080px; }
</style>
