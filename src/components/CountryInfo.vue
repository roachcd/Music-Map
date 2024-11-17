<template>
    <div class="page">
        <div class="data">
            <h1 id="countryName">Global</h1>
            <h3 id="countrySimilar">55% Similar</h3>
        </div>
    </div>
</template>
  
  <script>
  export default {
    name: 'CountryInfo',
    props: {
    }
  }
  </script>
  
  <style scoped>
    .page{
        background-color: rgb(184, 184, 184);
        position: fixed;
        width: 200px;
        margin-top: 1%;
        display: block;
        top: 0px;
        z-index: 1000;
        pointer-events: none;
        border-radius: 10px;
        margin-left: 20px;
        opacity: .9;
        -webkit-backdrop-filter: blur(20px);
        backdrop-filter: blur(20px);
    }
    .data{
        opacity: 1;
        color: black;
    }
    .data h1{
        filter: drop-shadow(0 1mm 3mm rgb(90, 90, 90));
        height: 40px;
        overflow-y: hidden;
        margin-bottom: -10px;
    }
  </style>
  