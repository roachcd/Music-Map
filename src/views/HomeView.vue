<template>
  <div class="home">
    <div id="map"></div>
    <CountryInfo :country-name="countryName"></CountryInfo>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import { latLng } from 'leaflet';
import CountryInfo from '@/components/CountryInfo.vue';


var weightData = require("@/assets/WeightData/Global.json");
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
    console.log("Created");
};

export default {
  name: 'HomeView',
  components: {
    CountryInfo
  },
  data(){
      return {
      };
  },
  methods:{
    setupLeafletMap: function () {
      const map = L.map('map', {zoomControl: false}).setView([0, 0], 2);

      const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 5,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(map);

      var countryData = require("@/assets/globe.geo.json")
      countryMap = new L.geoJson(countryData, {style: this.style, onEachFeature: this.hover});
      countryMap.addTo(map);

      info.addTo(map);    
      this.infoOnAdd(map);  
    },
    hover(feature, layer){
      this.onEachFeature(feature, layer)
    },
    style(feature) {
      return {
            fillColor: this.getColor(feature.properties.name),
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3',
            fillOpacity: 0.7
        };
    },
    getColor(country) {
      const result = weightDataJson.filter(item => item.name === country);

      if(result.length != 0){
        const d = result[0].weight;

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
        return '#d9d9d9';
      }
    },
    onEachFeature(feature, layer) {
        layer.on({
            mouseover: this.highlightFeature,
            mouseout: this.resetHighlight,
            click: this.zoomToFeature,
        });
    },
    zoomToFeature(e) {
        map.fitBounds(e.target.getBounds());
    },
    resetHighlight(e) {
        this.updateInfo("Global");
        //countryMap.resetStyle(e.target);
    },
    highlightFeature(e) {
        var layer = e.target;
        this.updateInfo(layer.feature.properties.name);

        layer.setStyle({
            weight: 5,
            color: '#666',
            dashArray: '',
            fillOpacity: 0.7
        });

        layer.bringToFront();
    },
    dataExists(country){
      const result = weightDataJson.filter(item => item.name === country);
      if(result.length != 0){
        return true;
      }
      return false;
    },
    updateInfo(props) {
      if(this.dataExists(props)){
        document.getElementById("countryName").textContent=props;
      }
      getWeightData(props);
      countryMap.resetStyle();
    },
    infoOnAdd(map) {
      resetHighlight();
    }
  },
  mounted() {
    this.setupLeafletMap();
    this.updateInfo("Global");
  },
}
</script>

<style>
  body {
      padding: 0;
      margin: 0;
  }
  html, body, #map {
      height: 100vh;
      width: 100%;
  }
  home{
    height: 100vh;
  }
  #map{
    background-color: #aad3df;
  }
</style>
